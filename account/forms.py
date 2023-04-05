from django import forms
from .models import Account

class RegistrForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'plaseholder':'password',
            }
        ),max_length=100
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'plaseholder':'confirm password',
            }
        ),max_length=100
    )
    class Meta:
        model = Account
        fields = ("first_name", "last_name", "phone_number", "password", "confirm_password")

    
    def clean(self):
        cleaned_data = super(RegistrForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")

    def __init__(self, *args, **kwargs):
        super(RegistrForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
