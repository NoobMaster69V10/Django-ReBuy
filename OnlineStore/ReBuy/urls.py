from django.urls import path
from .views import *

urlpatterns = [
    path('', MainPage.as_view(), name="main-page"),
    path('daily-all/', SeeAll.as_view(), name="daily_all"),
    path('category/<int:cat>', AllCategories.as_view(), name="category_page"),
    path('product/<slug:slug>', ProductView.as_view(), name="product_view"),
    path('search/<str:search_word>', SearchView.as_view(), name="search_view"),
    path('sign-in/', SignIn.as_view(), name="sign_in"),
    path('sign-up/', SignUp.as_view(), name="sign_up"),
    path('cart/', Cart.as_view(), name="cart"),
    path('cart/add/<slug:slug>', CartAdd.as_view(), name="cart_add"),
    path('cart/buy/<slug:slug>', CartBuy.as_view(), name="buy"),
    path('cart/remove/<slug:slug>', CartRemove.as_view(), name="remove"),
]
