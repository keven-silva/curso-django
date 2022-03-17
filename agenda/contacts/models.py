from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=20)
    last_name = models.CharField(
        verbose_name=("Last Name"), max_length=20, blank=True)
    phone = models.CharField(verbose_name=("Phone Number"), max_length=15)
    email = models.EmailField(verbose_name=(
        "Email"), max_length=255, blank=True)
    creation_date = models.DateTimeField(
        verbose_name=("Creation Date"), auto_created=True, auto_now=True)
    description = models.TextField(verbose_name=("Description"), blank=True)
    category = models.ForeignKey(Category, verbose_name=(
        "Category"), on_delete=models.DO_NOTHING)
    show = models.BooleanField(verbose_name=("Show"), default=True)
    image = models.ImageField(verbose_name=("Image"), blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.name
