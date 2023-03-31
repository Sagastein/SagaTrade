
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import index, details, contact, signup, new, dashboard, delete, edit, browse, logout_user
from .forms import LoginForm

app_name = 'home'

urlpatterns = [
    path("", index, name="index"),
    path("signup", signup, name="signup"),
    path('browse', browse, name="browse"),
    path('new/', new, name="new"),
    path('dashboard/', dashboard, name="dashboard"),
    path("contact/", contact, name="contact"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html",
         authentication_form=LoginForm), name="login"),
    path('logout/', logout_user, name="logout"),
    path('<int:pk>/delete/', delete, name="delete"),
    path('<int:pk>/edit/', edit, name="edit"),
    path('<int:pk>/', details, name="details"),

]
