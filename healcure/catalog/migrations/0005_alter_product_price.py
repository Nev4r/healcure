# Generated by Django 4.0.5 on 2022-07-11 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_category_name_alter_product_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True, verbose_name='Цена'),
        ),
    ]
