# Generated by Django 3.1.7 on 2021-03-06 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, choices=[('available', 'available'), ('sold', 'sold'), ('rented', 'rented')], max_length=50, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_price_day', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lms_app.categ')),
            ],
        ),
    ]
