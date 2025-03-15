# Generated by Django 5.0.4 on 2024-05-03 13:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_rename_product_comment_education'),
        ('ordering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(blank=True, default=1, null=True)),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.education')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='ordering.order')),
            ],
        ),
    ]
