from django import forms

from .models import Portfolio
from .models import StockAsset

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
        'quantity'
        ]
