from django.contrib.auth import get_user_model
from django.forms import ModelForm


class CustomSignupForm(ModelForm):
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        user.save()

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)

