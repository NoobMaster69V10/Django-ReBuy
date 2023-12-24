from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
from .forms import *


class MainPage(View):
    def get(self, request):
        slider_img = MainPageSlider.objects.all()
        categories = Categories.objects.filter(id__lte=7)
        daily_deals = Product.objects.filter(daily_deal=True, id__lte=17)
        form = SearchForm()
        return render(request, "ReBuy/index.html", {"slider_img": slider_img,
                                                    "categories": categories,
                                                    "daily_deals": daily_deals,
                                                    "form": form})

    def post(self, request):
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
        else:
            form = SearchForm()
        return redirect(f"search/{form.cleaned_data['search_text']}", {"form": form})


class SeeAll(ListView):
    model = Product
    slug_field = "url"
    template_name = "ReBuy/daily_all.html"

    def get_context_data(self, **kwargs):
        form = SearchForm()
        products = Product.objects.all()
        return {"products": products, "form": form}


class ProductView(DetailView):
    model = Product
    slug_field = "url"
    template_name = "ReBuy/product.html"
    context_object_name = "product"


class AllCategories(View):
    def get(self, request, cat):
        products = Product.objects.filter(category=cat).all()
        category = Categories.objects.exclude(id=cat).all()
        cat_name = Categories.objects.filter(id=cat).first()
        form = SearchForm()
        return render(request, "ReBuy/category.html",
                      {"products": products, "category": category, "cat_name": cat_name, "form": form})


class SearchView(View):
    def get(self, request, search_word):
        products = Product.objects.filter(title__icontains=search_word)
        form = SearchForm()
        return render(request, "ReBuy/search.html", {"search_word": search_word, "products": products, "form": form})

    def post(self, request):
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
        else:
            form = SearchForm()
        return redirect(f"search/{form.cleaned_data['search_text']}", {"form": form})


class SignIn(View):
    def get(self, request):
        form = SignInForm()
        return render(request, 'ReBuy/sign_in.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignInForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                if User.objects.filter(username=username, password=password):
                    return redirect('/')
                else:
                    return redirect("/sign-in/")


class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'ReBuy/sign_up.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                if form.cleaned_data['password'] == form.cleaned_data['password_again']:
                    username = form.cleaned_data['username']
                    email = form.cleaned_data['email']
                    password = form.cleaned_data['password']
                    User.objects.create(username=username, email=email, password=password)
                    return redirect('/sign-in/')
                else:
                    return redirect('/sign-up/')


class Cart(View):
    def get(self, request):
        form = SearchForm()
        cart = Product.objects.filter(cart=True)
        return render(request, 'ReBuy/cart.html', {"cart": cart, "form": form})


class CartAdd(View):
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        product.cart = True
        product.save()
        return HttpResponse("<h1>Product added to cart</h1><br><a href='/'>Back to home</a>")


class CartBuy(View):
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        product.cart = False
        product.save()
        return HttpResponse("<h1>You've bought product </h1><br><a href='/cart/'>Back to cart</a>")


class CartRemove(View):
    def get(self, request, slug):
        product = Product.objects.get(url=slug)
        product.cart = False
        product.save()
        return redirect('/cart/')
