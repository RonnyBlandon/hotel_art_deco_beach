from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class HomeReserveForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': _('Name')
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': _('Email')
        })
    )
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("The phone number must be entered in the format: '+999999999'.")
    )
    phone = forms.CharField(
        validators=[phone_validator],
        max_length=17,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': _('Phone')
        })
    )
    rooms = forms.ChoiceField(
        choices=[(_('No. of Rooms'), _('No. of Rooms')), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    adults = forms.ChoiceField(
        choices=[(_('No. of Adults'), _('No. of Adults')), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_start = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_end = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': _('Message'), 
            'rows': 4
        })
    )


class SubscriptionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Enter your email'),
                'class': 'form-control'
            }
        )
    )
    