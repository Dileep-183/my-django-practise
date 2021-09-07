from .models import Moblies
from django import forms



class MobliesForm(forms.ModelForm):
    class Meta:
        model = Moblies
        fields = "__all__"