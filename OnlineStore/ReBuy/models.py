from django.db import models
from django.urls import reverse


class Categories(models.Model):
    """Categories"""
    title = models.CharField("Category", max_length=150)
    image = models.ImageField("Category image", upload_to="categories/", null=True)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse("category_page", kwargs={"cat": self.pk})


class Product(models.Model):
    """Products"""
    title = models.CharField("Product name", max_length=300)
    description = models.TextField("Description")
    price = models.SmallIntegerField("Price", null=True)
    poster = models.ImageField("Poster", upload_to="re-buy/")
    category = models.ForeignKey(Categories, verbose_name="Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=150, unique=True)
    daily_deal = models.BooleanField("Daily Deal", default=False)
    cart = models.BooleanField("In Cart", default=False, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def get_absolute_url(self):
        return reverse("product_view", kwargs={"slug": self.url})


class ProductShots(models.Model):
    """Product shots"""
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    image = models.ImageField("Image", upload_to="re-buy-images/")

    class Meta:
        verbose_name = "Product Shot"
        verbose_name_plural = "Product Shots"


class MainPageSlider(models.Model):
    """Main page slider images"""
    name = models.CharField("Image name", max_length=100)
    image = models.ImageField("Main slider image", upload_to="main-slider/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Main page slider image"
        verbose_name_plural = "Main page slider images"


class User(models.Model):
    """User info"""
    username = models.CharField("Username", max_length=150, unique=True)
    email = models.CharField("Email", max_length=100, null=True)
    password = models.CharField("Password", max_length=100)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
