from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, related_name="sub_category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField( max_length=50)
    content = models.TextField()
    category = models.ForeignKey(Category, related_name="content", on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name="content", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    