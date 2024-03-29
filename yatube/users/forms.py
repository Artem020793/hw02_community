from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class PasswordChangingForm(PasswordChangeForm):
    fields = ('now_password', 'new_password', 'new_password_again')
