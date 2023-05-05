from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput



class custom_login_form(forms.Form):

    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(required=True, widget=PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        users = User.objects.filter(username=username).exists()
        print(not users)
        if not users:
            print('+++++++++++++++++++++++++++++++++')
            raise forms.ValidationError("Bunday foydalanuvchi topilmadi.")
        else:
            print('----------------------------------')
            return username
    

    def clean_password(self):
        print('clean-password-enter')
        password = self.cleaned_data['password']
        username = self.cleaned_data.get('username')
        if username:
            print(password)
            print(username)
            user = User.objects.filter(username=username).first()
            if not user.check_password(password):
                raise forms.ValidationError('Parol noto\'g\'ri kiritildi')
        return password


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=120, required=True)
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Bu foydalanuvchi nomi allaqachon band qilingan')
        else:
            return username
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if password.isnumeric():
            raise forms.ValidationError('Parolda kamida bitta harf qatnashishi kerak')
        elif password.isalpha():
            raise forms.ValidationError('Parolda kamida bitta son qatnashishi kerak')
        return password
    
    def clean_password_confirmation(self):
        password = self.data['password']
        password_confirmation = self.cleaned_data['password_confirmation']
        if password == password_confirmation:
            return password_confirmation
        raise forms.ValidationError('Tasdiqlash paroli noto\'g\'ri kiritildi')