# Generated by Django 5.0.4 on 2024-05-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm_app', '0002_alter_product_cat_alter_product_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=0, upload_to='image'),
            preserve_default=False,
        ),
    ]
