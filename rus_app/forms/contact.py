from django import forms


class Contact(forms.Form):
    anti_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    anti_email = forms.EmailField(max_length=50, required=True,
                                  widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    anti_subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Тема'}))
    anti_message = forms.CharField(max_length=1000, required=True,
                                   widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}))
