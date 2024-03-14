from django.urls import path
from .views import *


urlpatterns =[

    path('login/', login_view, name='logout_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_user, name='register_user'),
    path('retrieve_user/<int:pk>/',RetrieveUser.as_view()),
    path('update_user/<int:pk>/',UpdateUser.as_view()),
    path('delete_user/<int:pk>/',DeleteUser.as_view()),
    path('activate/<str:uidb64>/<str:token>/', activate_user, name='activate_user'),

    
]