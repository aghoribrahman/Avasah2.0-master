# Generated by Django 4.1.2 on 2023-06-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_contact_model_created_at_query_model_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='query_model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
