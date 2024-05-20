# Generated by Django 3.0.3 on 2024-04-26 15:25

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
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('category_type_id', models.PositiveIntegerField()),
                ('category_type_key', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('image_url', models.URLField(max_length=500)),
                ('categories', models.ManyToManyField(related_name='restaurants', to='restaurant_reviews.Category')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant_reviews.District')),
            ],
        ),
    ]
