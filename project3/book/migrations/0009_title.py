# Generated by Django 4.0.6 on 2023-02-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_fourth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
            ],
        ),
    ]
