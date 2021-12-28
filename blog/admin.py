from django.contrib import admin
from blog.models import Category, SubCategory, Content
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Content)
