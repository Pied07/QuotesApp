# Generated by Django 5.1 on 2024-08-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuotePage', '0004_alter_quote_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='caption',
            field=models.TextField(blank=True, default=models.CharField(max_length=200), max_length=1000, null=True),
        ),
    ]
