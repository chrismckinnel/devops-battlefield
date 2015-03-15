from django import forms


class InstanceForm(forms.Form):
    user_id = forms.IntegerField()
