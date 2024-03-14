from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, smart_str
from django.template.loader import render_to_string
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from blog.models import *
import uuid
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token



#-----------------------View for user to login page ----------------
# @api_view(['POST'])
# @permission_classes([])
# def login_view(request):
#     if request.user.is_authenticated:
#         return Response({"status": "error", "message": "User is already authenticated."}, status=status.HTTP_400_BAD_REQUEST)

#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(request, username=username, password=password)

#     if user is not None:
#         login(request, user)

#         # Generate a new token for the authenticated user
#         user.token = uuid.uuid4()
#         user.save()

#         return Response({
#             "status": "success",
#             "message": "Login successful.",
#             "token": str(user.token)
#         }, status=status.HTTP_200_OK)
#     else:
#         return Response({"status": "error", "message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)

#-------------------Logs out for current users logged in---------------------
@api_view(['POST'])
def logout_view(request):
    logout(request)

    # Revoke the token (optional)
    user = request.user
    if user.is_authenticated:
        user.token = None
        user.save()

    return Response({"status": "success", "message": "Logout successful."}, status=status.HTTP_200_OK)

#-----------------------Update User---------------------
class UpdateUser(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)  
    authentication_classes=(TokenAuthentication,)
    queryset= User.objects.all()
    serializer_class=UserSerializer

    def get_object(self):
        return self.request.user
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#--------------------Delete User---------------------

class DeleteUser(generics.DestroyAPIView):
    permission_classes = (AllowAny,)  
    authentication_classes=(TokenAuthentication)
    queryset= User.objects.all()
    serializer_class=UserSerializer


    
#--------------------------Retrieve Current User Profile-----------------------
class RetrieveUser(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)  
    authentication_classes = (TokenAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

#-----------------------------------Register User------------------------------
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        activation_token = generate_activation_token(user)
        current_site = get_current_site(request)

        PasswordResetToken.objects.create(user=user, token=activation_token)

        send_activation_email(user, activation_token, current_site)

        return Response({"status": "success", "message": "User registered successfully. Check your email for activation."}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------Activating the email of a new registered account----------------
def generate_activation_token(user):
    token = str(uuid.uuid4())
    return token

# -------------------send_activation_email-----------------
def send_activation_email(user, activation_token, current_site):
    subject = 'Activate Your Account'
    message = render_to_string('blog/activation_email.html', {
        'user': user,
        'protocol': 'http',  
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': activation_token,
    })
    user.email_user(subject, message)

#
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
@csrf_exempt
def activate_user(request, uidb64, token):
    try:
        uid = smart_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        password_reset_token = PasswordResetToken.objects.get(user=user, token=token)
        
        expiration_time = 24 * 60 * 60  # 24 hours in seconds

        if not user.is_email_verified and (timezone.now() - password_reset_token.created_at).total_seconds() < expiration_time:
            user.is_email_verified = True
            user.save()
            password_reset_token.delete()
            return Response({'message': 'Account activated successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, PasswordResetToken.DoesNotExist):
        return Response({'message': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)
    

# ------------------------Post View-------------------------

# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
# def post_view(request):
#     if request.method == 'POST':
#         post_serializer=PostSerializer(data=request.data)
#         if post_serializer.is_valid():
#             post_serializer.save()
#             return Response({"message":"Post was published","post":post_serializer.data},201)
#         return Response({ post_serializer.errors,400})
    
#     elif request.method=='GET':
#         posts = Post.get_all_posts()
#         # posts = Post.objects.all()
    
#         serialized_post=PostSerializer(posts, many=True).data
#         return Response({"data": serialized_post, "message": "success"},200 )


# @api_view(['GET','PUT','DELETE'])
# @permission_classes([AllowAny,])

# def get_edit_delete(request, id):
    
#     post = Post.objects.filter(id=id).first()
#     # first method  to return first object when you expect at most one object

# # GET Method
#     if request.method == 'GET':
#         post_serialized = PostSerializer(post).data
#         return  Response({"Data ":post_serialized}, status=200)
    
# # PUT Method
#     elif request.method == 'PUT':
#         post_serialized = PostSerializer(instance=post , data=request.data)
#         if post_serialized.is_valid():
#             post_serialized.save()
#             return Response({"message":"Edit Done Successfuly","Post":post_serialized.data},200)
#         return Response(post_serialized.errors, status=400)
# # DELETE Method
#     else:  
#         post.delete()
#         return Response({"message":"The Post was deleted","object Deleted":post.id})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_publish(request):
    if request.method == 'POST':
        request.data['author'] = request.user.id
        post_serializer = PostSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            
            # Retrieve the token associated with the authenticated user
            user_token = Token.objects.get(user=request.user)
            
            # Include token in the response
            response_data = {
                "message": "Post published successfully",
                "post": post_serializer.data,
            }
            return Response(response_data, status=201)
        return Response(post_serializer.errors, status=400)
    
@api_view(['GET'])
@permission_classes([AllowAny])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True).data
        return Response({"data": serialized_posts, "message": "success"}, status=200)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response({"message": "Post not found"}, status=404)

    if request.method == 'GET':
        post_serialized = PostSerializer(post).data
        return Response({"Data": post_serialized}, status=200)
    
    elif request.method == 'PUT':
        # Check if the current user is the author of the post
        if request.user == post.author:
            post_serialized = PostSerializer(instance=post, data=request.data)
            if post_serialized.is_valid():
                post_serialized.save()
                return Response({"message": "Post updated successfully", "Post": post_serialized.data}, status=200)
            return Response(post_serialized.errors, status=400)
        else:
            return Response({"message": "You are not authorized to update this post"}, status=403)

    elif request.method == 'DELETE':
        # Check if the current user is the author of the post
        if request.user == post.author:
            post.delete()
            return Response({"message": "The post was deleted", "object_deleted": id}, status=200)
        else:
            return Response({"message": "You are not authorized to delete this post"}, status=403)
        

from rest_framework import viewsets
from .customPermession import IsAuthor


class PostsView(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    




@api_view(['POST'])
@permission_classes([])
def login_view(request):
    if request.user.is_authenticated:
        return Response({"status": "error", "message": "User is already authenticated."}, status=status.HTTP_400_BAD_REQUEST)

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        # Check if a token already exists for the user
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "status": "success",
            "message": "Login successful.",
            "token": token.key
        }, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "message": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)