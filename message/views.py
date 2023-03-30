from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from home.models import Item
from message.form import ConversationForm
from message.models import Conversation

# Create your views here.

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    print(conversations)
    return render(request, 'inbox.html',
                  {'conversations': conversations})

@login_required()
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    if item.createdBy == request.user:
        return redirect('home:dashboard')

    conversations = Conversation.objects.filter(
        item=item).filter(members__in=[request.user.id])
    if conversations:
        pass

    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.createdBy)
            conversation.save()

            conversation_massage = form.save(commit=False)
            conversation_massage.conversation = conversation
            conversation_massage.createdBy = request.user
            conversation_massage.save()
            return redirect('home:details', pk=item_pk)
    else:
        form = ConversationForm()
        return render(request, 'new.html',{
                'form': form
            })
@login_required()
def detail(request,pk):
    conversation = Conversation.objects.filter(
        members__in=[request.user.id]).get(pk=pk)
    if request.method == 'POST':
        form = ConversationForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.createdBy = request.user
            conversation_message.save()

            conversation.save()

            return redirect('message:detail', pk=pk)
    else:
        form = ConversationForm()

    return render(request, 'detail.html',{
            'conversation': conversation,
            'form':form
    }
    )
