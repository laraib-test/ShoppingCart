

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Product,
    Category,
    Store,
    Cart,
    CartItem
)
from .models import Price
from .forms import PriceForm,StoreForm
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404

def register(request):
    return render(request, 'register.html')
def home(request):

    context = {

        "products_count": Product.objects.count(),
        "stores_count": Store.objects.count(),
        "categories_count": Category.objects.count(),
        "categories": Category.objects.all(),

    }

    return render(
        request,
        "home.html",
        context
    )
@login_required
def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:

        item.quantity += 1
        item.save()

    return redirect('product_list')

@login_required
def cart_view(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    return render(
        request,
        "shoppinglist/cart.html",
        {
            "cart": cart
        }
    )
@login_required
def update_cart_item(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if request.method == "POST":

        quantity = int(
            request.POST.get("quantity", 1)
        )

        if quantity > 0:

            item.quantity = quantity
            item.save()

        else:

            item.delete()

    return redirect("cart")


@login_required
def remove_cart_item(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect("cart")


def load_products(request):
    category_id = request.GET.get("category")
    products = Product.objects.filter(category_id=category_id).order_by("name")
    return render(
        request,
        "shoppinglist/partials/product_dropdown_list.html",
        {"products": products}
    )

# ADDED: Your missing Price creation view with form context support
class PriceCreateView(
    SuccessMessageMixin,
    CreateView
):

    model = Price

    form_class = PriceForm

    template_name = "shoppinglist/price_form.html"

    success_url = reverse_lazy("price_add")

    success_message = "Price added successfully!"

class PriceUpdateView(UpdateView):

    model = Price

    form_class = PriceForm

    template_name = "shoppinglist/price_form.html"

    success_url = reverse_lazy("price_comparison")

    def get_initial(self):

        initial = super().get_initial()

        initial["category"] = self.object.product.category

        initial["product_name"] = self.object.product.name

        return initial

class PriceDeleteView(DeleteView):

    model = Price

    template_name = "shoppinglist/price_confirm_delete.html"

    success_url = reverse_lazy("price_comparison")

class CategoryProductListView(ListView):
    model = Product
    template_name = 'shoppinglist/category_products.html'
    context_object_name = 'products'

    def get_queryset(self):
        self.category = Category.objects.get(id=self.kwargs['pk'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
    
    
class StoreListView(ListView):
    model = Store
    template_name = 'shoppinglist/store_list.html'
    context_object_name = 'stores'


class ProductListView(ListView):
    model = Product
    template_name = 'shoppinglist/product_list.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product

    fields = [
        'category',
        'name',
        'quantity',
        'unit',
        #'price',#
        'image'
    ]

    template_name = 'shoppinglist/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product

    fields = [
        'category',
        'name',
        'quantity',
        'unit',
        #'price',
        'image'
    ]

    template_name = 'shoppinglist/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'shoppinglist/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
class CategoryListView(ListView):

    model = Category

    template_name = 'shoppinglist/category_list.html'

    context_object_name = 'categories'

class CategoryCreateView(CreateView):

    model = Category

    fields = ['name', 'image']

    template_name = 'shoppinglist/category_form.html'

    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):

    model = Category

    fields = ['name', 'image']

    template_name = 'shoppinglist/category_form.html'

    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):

    model = Category

    template_name = 'shoppinglist/category_confirm_delete.html'

    success_url = reverse_lazy('category_list')

class StoreCreateView(CreateView):

    model = Store

    form_class = StoreForm

    template_name = 'shoppinglist/store_form.html'

    success_url = reverse_lazy('store_list')
class StoreUpdateView(UpdateView):

    model = Store

    form_class = StoreForm

    template_name = 'shoppinglist/store_form.html'

    success_url = reverse_lazy('store_list')

class StoreDeleteView(DeleteView):

    model = Store

    template_name = 'shoppinglist/store_confirm_delete.html'

    success_url = reverse_lazy('store_list')

   

class PriceComparisonView(TemplateView):

    template_name = "shoppinglist/price_comparison.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        products = Product.objects.all()

        comparison_data = []

        for product in products:

            prices = Price.objects.filter(product=product)

            product_prices = {}

            cheapest_price = None
            cheapest_store = None

            for p in prices:

                product_prices[p.store.name] = {
                    "price": p.price,
                    "id": p.id
                }

                if cheapest_price is None or p.price < cheapest_price:

                    cheapest_price = p.price
                    cheapest_store = p.store.name

            comparison_data.append({

                "product": product,
                "prices": product_prices,
                "cheapest_price": cheapest_price,
                "cheapest_store": cheapest_store,

            })

        context["comparison_data"] = comparison_data

        return context



