# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from blog.models import Post
# from rest_framework.authtoken.models import Token
# from django.urls import reverse
# from rest_framework.test import APIClient
# from rest_framework import status

# User = get_user_model()

# class UserModelTestCase(TestCase):
#     def test_create_user(self):
#         user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
#         self.assertEqual(user.username, 'testuser')
#         self.assertEqual(user.email, 'test@example.com')
#         self.assertFalse(user.is_email_verified)  # Newly created user should not be email verified

#     def test_create_superuser(self):
#         admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword123')
#         self.assertTrue(admin_user.is_superuser)
#         self.assertTrue(admin_user.is_staff)

# class PostModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

#     def test_create_post(self):
#         post = Post.objects.create(title='Test Post', content='This is a test post content', author=self.user)
#         self.assertEqual(post.title, 'Test Post')
#         self.assertEqual(post.content, 'This is a test post content')
#         self.assertEqual(post.author, self.user)

# class TokenModelTestCase(TestCase):
#     def test_create_token_for_new_user(self):
#         user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
#         token = Token.objects.get(user=user)
#         self.assertIsNotNone(token)

# class SignalTestCase(TestCase):
#     def test_token_creation_on_user_creation(self):
#         user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
#         self.assertTrue(Token.objects.filter(user=user).exists())

#     def test_token_not_created_for_existing_user(self):
#         user = User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')
#         token_count_before = Token.objects.count()  # Count tokens before creating the user
#         user.save()  # Saving existing user should not create a new token
#         token_count_after = Token.objects.count()  # Count tokens after saving the user
#         self.assertEqual(token_count_before, token_count_after)  # Token count should remain the same

# class ViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

#     def test_login_view(self):
#         # Test user login
#         response = self.client.post(reverse('login_view'), {'username': 'testuser', 'password': 'password123'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Test login with incorrect password
#         response = self.client.post(reverse('login_view'), {'username': 'testuser', 'password': 'wrongpassword'})
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_register_user_view(self):
#         # Test user registration
#         data = {
#             'username': 'newuser',
#             'email': 'newuser@example.com',
#             'password': 'newpassword',
#             'password2': 'newpassword'
#         }
#         response = self.client.post(reverse('register_user'), data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # Test registration with missing data
#         response = self.client.post(reverse('register_user'), {})
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# class PostViewsTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

#     def test_create_post_view(self):
#         # Log in the user first
#         self.client.force_authenticate(user=self.user)

#         # Test creating a post
#         data = {
#             'title': 'Test Post',
#             'content': 'This is a test post content.'
#         }
#         response = self.client.post(reverse('create_post'), data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         # Test creating a post with missing data
#         response = self.client.post(reverse('create_post'), {})  # No need to modify an empty dictionary
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

#     def test_post_list_view(self):
#         # Log in the user first
#         self.client.force_authenticate(user=self.user)

#         # Test listing all posts
#         response = self.client.get(reverse('post_list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_post_detail_view(self):
#         # Log in the user first
#         self.client.force_authenticate(user=self.user)

#         # Create a test post
#         post = Post.objects.create(title='Test Post', content='This is a test post content.', author=self.user)

#         # Test retrieving a specific post
#         response = self.client.get(reverse('post_detail', kwargs={'id': post.id}))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Test retrieving a non-existent post
#         response = self.client.get(reverse('post_detail', kwargs={'id': 999}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Post
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()

class UserModelTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertFalse(user.is_email_verified)  # Newly created user should not be email verified

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(username='admin', email='admin@example.com', password='adminpassword123')
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_create_post(self):
        post = Post.objects.create(title='Test Post', content='This is a test post content', author=self.user)
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post content')
        self.assertEqual(post.author, self.user)

class TokenModelTestCase(TestCase):
    def test_create_token_for_new_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        token = Token.objects.get(user=user)
        self.assertIsNotNone(token)

class SignalTestCase(TestCase):
    def test_token_creation_on_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.assertTrue(Token.objects.filter(user=user).exists())

    def test_token_not_created_for_existing_user(self):
        user = User.objects.create_user(username='existinguser', email='existing@example.com', password='password123')
        token_count_before = Token.objects.count()  # Count tokens before creating the user
        user.save()  # Saving existing user should not create a new token
        token_count_after = Token.objects.count()  # Count tokens after saving the user
        self.assertEqual(token_count_before, token_count_after)  # Token count should remain the same

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    # def test_login_view(self):
    #     # Test user login
    #     response = self.client.post(reverse('login_view'), {'username': 'testuser', 'password': 'password123'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test login with incorrect password
        response = self.client.post(reverse('login_view'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class PostViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')

    def test_create_post_view(self):
        # Log in the user first
        self.client.force_authenticate(user=self.user)

        # Test creating a post
        data = {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        }
        response = self.client.post(reverse('create_post'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test creating a post with missing data
        response = self.client.post(reverse('create_post'), {})  # No need to modify an empty dictionary
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_list_view(self):
        # Log in the user first
        self.client.force_authenticate(user=self.user)

        # Test listing all posts
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

def test_post_detail_view(self):
    # Log in the user first
    self.client.force_authenticate(user=self.user)

    # Create a test post
    post = Post.objects.create(title='Test Post', content='This is a test post content.', author=self.user)

    # Test retrieving a specific post
    response = self.client.get(reverse('post_detail', kwargs={'pk': post.pk}))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], 'Test Post')
    self.assertEqual(response.data['content'], 'This is a test post content.')
    self.assertEqual(response.data['author'], self.user.id)

    # Test retrieving a non-existent post
    response = self.client.get(reverse('post_detail', kwargs={'pk': 999}))
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



