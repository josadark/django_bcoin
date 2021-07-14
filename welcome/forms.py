from django import forms

from .models import Portfolio
from .models import StockAsset
from .models import Screen

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            'title',
            'description'
        ]

class AssetForm(forms.ModelForm):
    class Meta:
        model = StockAsset
        exclude = ('portfolio',)
        fields=[
        'ticker',
        'date_purchased',
        'quantity',
        'buyPrice'
        ]

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        exclude = ('user',)
        fields=[
        'title',
        'description',
        'minValue',
        'maxValue',
        'minVolume',
        'maxVolume'
        ]
