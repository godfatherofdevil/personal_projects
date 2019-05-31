# Generated by Django 2.2.1 on 2019-05-31 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('customer', 'customer'), ('consultant', 'consultant'), ('supplier', 'supplier'), ('superuser', 'superuser')], default='customer', max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='inactive', max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
