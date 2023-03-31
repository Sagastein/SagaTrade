
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import Category, Item, User
from .forms import SignUpForm, NewItemForm, EditItemForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_solid=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'items.html', {
        'items': items,
        'categories': categories
    })


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_solid=False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__contains=query) |
                             Q(description__contains=query))

    return render(request, 'browse.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def details(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item is None:
        return messages.error(request, 'No such item')
    related_item = Item.objects.filter(
        category=item.category, is_solid=False).exclude(pk=pk)[0:3]
    print(item)
    return render(request, 'details.html', {'item': item,
                                            "related_item": related_item})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            # email = form.cleaned_data.get('email')
            email = request.POST['email']
            print(email)
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email is already in use.')
            else:
                form.save()
                return redirect('/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {
        "form": form,
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.createdBy = request.user
            item.save()
            return redirect('home:details', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'itemform.html', {
        'form': form,
        'title': "New Item",
    },)


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            messages.info(request, 'data updated successfully.')
            return redirect('home:details', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'itemform.html', {
        'form': form,
        'title': "Edit Item",
    },)


@login_required()
def contact(request):
    return render(request, 'contact.html')


@login_required
def dashboard(request):
    items = Item.objects.filter(createdBy=request.user)
    return render(request, 'dashboard.html', {
                  "items": items
                  })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, createdBy=request.user)
    item.delete()
    messages.error(request, 'data deleted.')
    return redirect('home:dashboard')


def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out')
    return redirect('home:index')
