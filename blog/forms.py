from django import forms
from .models import Posta


class PostForm(forms.ModelForm):
    class Meta:
        model = Posta
        fields = ('usuario','titulua', 'testua','sortutako_data','publikatutako_data','image','publikatuta')
