# to allow users to authenticate using username or email

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            # Check if the username is an email
            user = user_model.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None
