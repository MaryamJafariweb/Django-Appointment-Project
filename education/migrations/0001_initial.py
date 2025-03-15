# Generated by Django 5.0.4 on 2024-04-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='education')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
