from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', PostsView, basename='post')

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
    path('create_post/',create_post,name= 'create_post'),
    path('post_list/',post_list,name= 'post_list'),
    path('post_detail/<int:id>',post_detail,name= 'post_detail'),

#--------- if use viewset instead regular function-----------------
    path('viewset/', include(router.urls)),



    
]