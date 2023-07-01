from django import forms

class FormUpload(forms.Form):
    file = forms.FileField()