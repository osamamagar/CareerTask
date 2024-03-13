from django.urls import path
from .views import *


urlpatterns =[

    path('register/', register_user, name='register_user'),
    path('edit_user/<int:pk>/',RetrieveUpdateDestroyUser.as_view()),
    path('delete_user/<int:pk>/',DeleteUser.as_view()),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('activate/<str:uidb64>/<str:token>/', activate_user, name='activate_user'),

    
]