# Generated by Django 5.0.6 on 2024-06-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTossi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
            ],
        ),
    ]
