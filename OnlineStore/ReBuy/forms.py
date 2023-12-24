from django import forms


class SearchForm(forms.Form):
    search_text = forms.CharField(label='search_text', max_length=150)


class SignInForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)


class SignUpForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    email = forms.EmailField(label="Email", max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    password_again = forms.CharField(label='Confirm', widget=forms.PasswordInput, max_length=100)
