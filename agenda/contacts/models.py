from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(verbose_name=("Name"), max_length=100)
    last_name = models.CharField(
        verbose_name=("Last Name"), max_length=100, blank=True)
    phone = models.CharField(verbose_name=("Phone Number"), max_length=15)
    email = models.CharField(verbose_name=(
        "Email"), max_length=255, blank=True)
    creation_date = models.DateTimeField(
        verbose_name=("Creation Date"), auto_created=True)
    description = models.TextField(verbose_name=("Description"), blank=True)
    category = models.ForeignKey(Category, verbose_name=(
        "Category"), on_delete=models.DO_NOTHING)
    show = models.BooleanField(verbose_name=("Show"), default=True)

    def __str__(self):
        return self.name
