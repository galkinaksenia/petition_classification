# Generated by Django 5.1.5 on 2025-01-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
