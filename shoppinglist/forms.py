from django import forms

from django import forms
from .models import Price, Store, Product, Category


class PriceForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "select select-bordered w-full"
            }
        )
    )

    product_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full",
                "placeholder": "🔎 Search product..."
            }
        )
    )

    class Meta:

        model = Price

        fields = [
            "store",
            "price",
        ]

        widgets = {

            "store": forms.Select(
                attrs={
                    "class": "select select-bordered w-full"
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "$ Enter price"
                }
            ),
        }

    def save(self, commit=True):

        price = super().save(commit=False)

        # ONLY create product when adding NEW price
        if not self.instance.pk:

            category = self.cleaned_data.get("category")

            product_name = self.cleaned_data.get(
                "product_name"
            )

            product, created = Product.objects.get_or_create(

                name=product_name.strip(),

                defaults={
                    "category": category,
                    "quantity": 1,
                    "unit": "pcs",
                }
            )

            price.product = product

        if commit:
            price.save()

        return price
class StoreForm(forms.ModelForm):
    
    class Meta:

        model = Store

        fields = [
            'name',
            'location',
            'logo',
            "address",
            "website"

        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full"
                }
            ),

        "location": forms.TextInput(
             attrs={
                 "class": "input input-bordered w-full",
                 "placeholder": "Enter store location"
                }
                  ),
         "logo": forms.ClearableFileInput(
                attrs={
                    "class": "file-input file-input-bordered w-full"
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": "textarea textarea-bordered w-full",
                    "placeholder": "Enter store address"
                }
            ),
            "website": forms.URLInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placeholder": "Enter website URL"
                }
            ),
        }
        