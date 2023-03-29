from django import forms

class registerForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length= 20, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=20,widget=forms.PasswordInput)
    
class loginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length= 20, widget=forms.PasswordInput)