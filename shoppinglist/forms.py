from django import forms
from .models import Price, Store, Product, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:

        model = User

        fields = (
            'username',
            'email',
            'password1',
            'password2',
        )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            field.widget.attrs.update({
                'class': 'input input-bordered w-full',
                'placeholder': f'Enter {field_name}',
            })


class ProductForm(forms.ModelForm):

    class Meta:

        model = Product

        fields = [
            'category',
            'name',
            'quantity',
            'unit',
            'image',
        ]

    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        duplicate = Product.objects.filter(
            name__iexact=name
        )

        if self.instance.pk:
            duplicate = duplicate.exclude(
                pk=self.instance.pk
            )

        if duplicate.exists():
            raise forms.ValidationError(
                "A product with this name already exists."
            )

        return name

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

    def clean(self):
        cleaned_data = super().clean()

        store = cleaned_data.get("store")
        product_name = cleaned_data.get("product_name")

        if store and product_name:
            existing_product = Product.objects.filter(
                name__iexact=product_name.strip()
            ).first()

            if existing_product:
                duplicate = Price.objects.filter(
                    store=store,
                    product=existing_product
                )

                # Ignore current object when editing
                if self.instance.pk:
                    duplicate = duplicate.exclude(
                        pk=self.instance.pk
                    )

                if duplicate.exists():
                    raise forms.ValidationError(
                        "This product already exists for this store."
                    )

        return cleaned_data

    def save(self, commit=True):
        price = super().save(commit=False)

        product_name = self.cleaned_data.get("product_name")
        category = self.cleaned_data.get("category")

        product = Product.objects.filter(
            name__iexact=product_name.strip()
        ).first()

        if not product:
            product = Product.objects.create(
                name=product_name.strip(),
                category=category,
                quantity=1,
                unit="pcs",
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
        
