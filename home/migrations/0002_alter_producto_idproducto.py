# Generated by Django 4.1.3 on 2022-11-01 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='idProducto',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]