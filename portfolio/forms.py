from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=70)
    email = forms.EmailField(max_length=150)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)