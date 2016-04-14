from django import forms


class Contact (forms.Form):
    contacter_name = forms.CharField(label='Your name')
    contacter_mail = forms.EmailField(label='Your email')
    contacter_message = forms.CharField(widget=forms.Textarea, label='Message')
