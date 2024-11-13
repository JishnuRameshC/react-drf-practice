from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)  # For the category image
    banner_image = models.ImageField(upload_to='category_banners/', blank=True, null=True)  # For the banner image
    meta_title = models.CharField(max_length=255, blank=True, null=True)  # SEO Title for the category page
    meta_description = models.TextField(blank=True, null=True)  # SEO Description for the category page

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('category_products', args=[self.slug])

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')  # Links to a Category
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='subcategory_images/', blank=True, null=True)  # For the subcategory image
    meta_title = models.CharField(max_length=255, blank=True, null=True)  # SEO Title for the subcategory page
    meta_description = models.TextField(blank=True, null=True)  # SEO Description for the subcategory page

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'Subcategories'

    def get_url(self):
        return reverse('subcategory_products', args=[self.slug])

    def __str__(self):
        return self.name
