from django import forms

from .models import Coffee


class CoffeeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Coffee
