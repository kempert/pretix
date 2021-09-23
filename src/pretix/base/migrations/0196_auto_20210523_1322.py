# Generated by Django 3.2.2 on 2021-05-23 13:22

import django.db.models.deletion
from django.db import migrations, models

import pretix.helpers.countries


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0195_auto_20210622_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoiceaddress',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_addresses', to='pretixbase.customer'),
        ),
        migrations.CreateModel(
            name='AttendeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('attendee_name_cached', models.CharField(max_length=255, null=True)),
                ('attendee_name_parts', models.JSONField(default=dict)),
                ('attendee_email', models.EmailField(max_length=254, null=True)),
                ('company', models.CharField(max_length=255, null=True)),
                ('street', models.TextField(null=True)),
                ('zipcode', models.CharField(max_length=30, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('country', pretix.helpers.countries.FastCountryField(countries=pretix.helpers.countries.CachedCountries, max_length=2, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('answers', models.JSONField(default=list)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendee_profiles', to='pretixbase.customer')),
            ],
        ),
    ]