from django import forms

class ContactForm(forms.Form):
    isim = forms.CharField(max_length=100)
    email = forms.EmailField()
    mesaj = forms.CharField(widget=forms.Textarea)