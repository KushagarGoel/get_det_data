from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()




class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Password'}))



    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Are you sure that you are registered.")
        return username

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        if user is not None and not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        elif user is None:
            pass
        else:
            return password


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password1 = forms.CharField(label='Password',widget= forms.PasswordInput(attrs={'placeholder':'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget= forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))

    class Meta:
        model = User
        fields = ['username','email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password Does Not Match")
        else:
            return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please Enter Email")
        user_count = User.objects.filter(email= email).count()
        if user_count > 0:
            raise forms.ValidationError("Email Already Exist")
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
