from django.urls import path
from .views import *


urlpatterns =[

#------------------------- Account --------------------------------
    
    path('login/', login_view, name='logout_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_user, name='register_user'),
    path('retrieve_user/<int:pk>/',RetrieveUser.as_view()),
    path('retrieve_user/', RetrieveUser.as_view(), name='retrieve_user'),
    path('update_user/<int:pk>/',UpdateUser.as_view(),name="update_user"),
    path('delete_user/<int:pk>/',DeleteUser.as_view(),name= "delete_user"),
    path('activate/<str:uidb64>/<str:token>/', activate_user, name='activate_user'),

#------------------------- Post --------------------------------
    path('create_post/',post_view,name= 'create_post'),
    path('get_post/',post_view,name= 'get_post'),
    path('edit_post/<int:id>/',get_edit_delete,name= 'edit_post'),
    path('delete_post/<int:id>/',get_edit_delete,name= 'delete_post'),
    path('get_post/<int:id>/',get_edit_delete,name= 'get_custom_post'),



    
]