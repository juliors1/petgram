from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'first_name', 'email']