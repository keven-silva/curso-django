# Generated by Django 4.0 on 2022-03-17 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_created=True, verbose_name='Creation Date')),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('last_name', models.CharField(blank=True, max_length=20, verbose_name='Last Name')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('show', models.BooleanField(default=True, verbose_name='Show')),
                ('image', models.ImageField(blank=True, upload_to='fotos/%Y/%m/', verbose_name='Image')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.category', verbose_name='Category')),
            ],
        ),
    ]
