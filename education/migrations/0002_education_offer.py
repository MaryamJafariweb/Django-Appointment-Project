# Generated by Django 5.0.4 on 2024-04-22 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='offer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
