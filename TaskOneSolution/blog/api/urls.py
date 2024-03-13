from django.urls import path
from .views import *


urlpatterns =[

    path('register/', register_user, name='register_user'),
    path('edit_user/<int:pk>/',RetrieveUpdateDestroyMyUser.as_view()),
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-login'),
    path('activate/<str:uidb64>/<str:token>/', activate_user, name='activate_user'),

    
]