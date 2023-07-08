from add_link.models import Add_link
from django import forms

class AddlinkForm(forms.ModelForm):
    class Meta:
        model = Add_link
        fields = ['link_for', 'link']