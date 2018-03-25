from django import forms
from gallery_app.models import Picture

class PictureModelForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['name']