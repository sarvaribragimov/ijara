from django import forms
from post.models import Kvartera
from django.forms import ModelForm
from django.forms import ModelChoiceField
from .models import Kvartera, Category

class KvarteraForm(forms.ModelForm):
    category = ModelChoiceField(queryset=Category.objects.all(), to_field_name='id')

    
    class Meta:
        model = Kvartera
        fields = "__all__"

    def clean(self):
        cleaned_data = super(KvarteraForm, self).clean()
    
    def __init__(self, *args, **kwargs):
        super(KvarteraForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"



