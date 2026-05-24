from django import views
from django.urls import path
from . import views

from .views import (
    PriceComparisonView,
    PriceDeleteView,
    PriceUpdateView,
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView, 
    CategoryDeleteView,
    StoreCreateView,
    StoreUpdateView,
    StoreDeleteView,
    StoreListView,     
    CategoryProductListView

)
from .views import add_to_cart, cart_view,update_cart_item, remove_cart_item
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView



urlpatterns = [
    
    path('', views.home, name='home'),  # homepage
    path(
    "logout/",
    LogoutView.as_view(next_page="home"),
    name="logout"
),
path('register/', views.register, name='register'),
    path('products/', ProductListView.as_view(), name='product_list'),
    #path('category/<int:pk>/products/',CategoryProductListView.as_view(),name='category_products'),
    #path('categories/', CategoryListView.as_view(), name='category_list'),
    path('stores/', StoreListView.as_view(), name='store_list'),
    path('add/', ProductCreateView.as_view(), name='product_add'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/remove/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path(
    "price/<int:pk>/edit/",
    views.PriceUpdateView.as_view(),
    name="price_edit",
),
    path(
        'categories/',
        CategoryListView.as_view(),
        name='category_list'
    ),

    path(
        'category/<int:pk>/products/',
        CategoryProductListView.as_view(),
        name='category_products'
    ),


path(
    'categories/add/',
    CategoryCreateView.as_view(),
    name='category_add'
),

path(
    'categories/<int:pk>/edit/',
    CategoryUpdateView.as_view(),
    name='category_edit'
),

path(
    'categories/<int:pk>/delete/',
    CategoryDeleteView.as_view(),
    name='category_delete'
),


# Store CRUD
path(
    'stores/',
    StoreListView.as_view(),
    name='store_list'
    ),

path(
    'stores/add/',
    StoreCreateView.as_view(),
    name='store_add'
),

path(
    'stores/<int:pk>/edit/',
    StoreUpdateView.as_view(),
    name='store_edit'),

    path(
    'stores/<int:pk>/delete/',
    StoreDeleteView.as_view(),
    name='store_delete'
),
path(
    'price/add/',
    views.PriceCreateView.as_view(),
    name='price_add'
),
path(
    "load-products/",
    views.load_products,
    name="load_products"
),
path(
    "compare/",
    PriceComparisonView.as_view(),
    name="price_comparison"
),
path(
    "price/edit/<int:pk>/",
    PriceUpdateView.as_view(),
    name="price_edit"
),

path(
    "price/delete/<int:pk>/",
    PriceDeleteView.as_view(),
    name="price_delete"
),
# CART
    path('cart/', cart_view, name='cart'),
# ADD TO CART
    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),
]