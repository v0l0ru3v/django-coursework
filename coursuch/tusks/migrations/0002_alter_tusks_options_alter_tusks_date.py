# Generated by Django 4.2.2 on 2023-06-19 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tusks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tusks',
            options={'verbose_name': ('Tusk',), 'verbose_name_plural': 'Tusks'},
        ),
        migrations.AlterField(
            model_name='tusks',
            name='date',
            field=models.DateTimeField(verbose_name='дедлайн'),
        ),
    ]
