from django.contrib.auth.hashers import make_password
from .models import *
from accounts.enums import RoleCodes
from django import forms




class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز', widget=forms.PasswordInput, required=False)
    class Meta:
        model = User
        fields = ('username', 'password1', 'email', 'role')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        if user.role.code == RoleCodes.ADMIN.value:
            user.is_superuser = True
        else:
            user.is_superuser = False
        if self.data.get("password1") is not None and self.data.get("password1") != '':
            password = make_password(self.cleaned_data["password1"])
            user.password = password
        if commit:
            user.save()
        return user
