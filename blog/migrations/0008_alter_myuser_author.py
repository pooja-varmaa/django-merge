# Generated by Django 4.0.3 on 2022-03-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_category_slug_alter_post_slug_alter_tag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='author',
            field=models.BooleanField(default=False),
        ),
    ]