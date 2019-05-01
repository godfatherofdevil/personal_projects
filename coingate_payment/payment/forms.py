from django import forms

class PriceForm(forms.Form):
    PRODUCT_CHOICES = [
        ('0', 'PRODUCT1'),
        ('1', 'PRODUCT2'),
        ('2', 'PRODUCT3'),
        ('3', 'PRODUCT4'),
        ('4', 'PRODUCT5')
    ]

    products = forms.ChoiceField(
        label='Product',
        widget=forms.Select, 
        choices=PRODUCT_CHOICES
        )
    
    price = forms.CharField(
        label="Quantity",
        max_length=60,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'How many products?'
        })
    )

