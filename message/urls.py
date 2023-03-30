from django.urls import path
from .views import new_conversation,inbox,detail

app_name = 'message'

urlpatterns = [
    path('',inbox,name='inbox'),
    path('<int:pk>/',detail,name='detail'),
    path('conv/<int:item_pk>/',new_conversation,name="conv")
]
