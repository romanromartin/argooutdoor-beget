from django import forms

class CallForm(forms.Form):
    username = forms.CharField(help_text= ('Обязательное поле.'),
                               widget=forms.TextInput(attrs={'placeholder': ('Имя')}),
                               required=True,
                               error_messages={'required': 'Не указано имя'})
    phone = forms.CharField(help_text= ('Формат 000-0000000.'),
                            widget=forms.TextInput(attrs={'placeholder': ('Телефон')}),
                            error_messages={'required': 'Не указан телефон'},
                            required=True)


