# Generated by Django 4.0.2 on 2023-01-24 14:28

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(verbose_name='本文'),
        ),
    ]
