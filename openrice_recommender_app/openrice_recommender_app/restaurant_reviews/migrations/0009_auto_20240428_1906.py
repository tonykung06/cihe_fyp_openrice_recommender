# Generated by Django 3.2.25 on 2024-04-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_reviews', '0008_remove_review_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
