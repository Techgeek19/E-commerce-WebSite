# Generated by Django 3.0.6 on 2020-05-22 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
