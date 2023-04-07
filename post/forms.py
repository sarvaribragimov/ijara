from django import forms
from .models import Kvartera

class KvarteraForm(forms.ModelForm):
    
    class Meta:
        model = Kvartera
        fields = "__all__"

    def clean(self):
        cleaned_data = super(KvarteraForm, self).clean()
    
    def __init__(self, *args, **kwargs):
        super(KvarteraForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
