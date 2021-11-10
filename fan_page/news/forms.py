from django import forms
from .models import *

class Coments_create(forms.ModelForm):

    class Meta:
        model = Comentaries
        fields = ['commentary']
        widgets={'commentary':forms.Textarea(attrs={'cols':100,'rows':2})}