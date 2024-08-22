from django import forms

class Users_Form(forms.Form):
    first_name = forms.CharField(help_text="Wura", max_length=100, required=True, label="First Name")
    last_name = forms.CharField(help_text="Pascal", max_length=100, required=True, label="Last Name")
    email = forms.EmailField(help_text="pascal@", max_length=100, required=True, label="Email Name")
    gender = forms.CheckboxInput()
    password = forms.CharField(widget=forms.PasswordInput())



class NameForm(forms.Form):
    full_name = forms.CharField( max_length=20)
    class_grade = forms.CharField( max_length=50)
    age = forms.CharField( max_length=10)
    name_school = forms.CharField( max_length=30)


# class Wura_Form(forms.Form):
    first_name = forms.CharField(help_text="Wura", max_length=100, required=True, label="First Name")
    last_name = forms.CharField(help_text="Pascal", max_length=100, required=True, label="Last Name")
    email = forms.EmailField(help_text="pascal@", max_length=100, required=True, label="Email Name")
    gender = forms.CheckboxInput()
    password = forms.PasswordInput()