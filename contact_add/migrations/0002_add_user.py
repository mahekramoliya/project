# Generated by Django 5.0 on 2023-12-15 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_add', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_by', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
            ],
        ),
    ]