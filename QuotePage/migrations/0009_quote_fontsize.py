# Generated by Django 5.1 on 2024-08-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePage', '0008_quote_fontcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='fontsize',
            field=models.IntegerField(default=20),
        ),
    ]
