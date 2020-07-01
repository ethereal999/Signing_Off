from django import forms
from .models import College


class UserForm(forms.Form):
    college_name = forms.ChoiceField(choices=[])
    email = forms.EmailField(max_length=200, required=True)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['college_name'].choices = [(x.name,x.name) for x in College.objects.all()]