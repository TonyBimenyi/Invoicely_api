# Generated by Django 4.0.2 on 2022-02-23 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField(default=1)),
                ('client_name', models.CharField(max_length=200)),
                ('client_email', models.CharField(max_length=250)),
                ('client_org_number', models.CharField(max_length=250)),
                ('client_adress', models.CharField(max_length=250)),
                ('client_country', models.CharField(max_length=200)),
                ('client_contact', models.CharField(max_length=200)),
                ('invoice_type', models.CharField(choices=[('invoice', 'Invoice'), ('credit_note', 'Credit note')], default='invoice', max_length=250)),
                ('due_days', models.IntegerField(default=14)),
                ('is_sent', models.BooleanField(default=False)),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('vat_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('discount_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='api.abakiriya')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_invoices', to=settings.AUTH_USER_MODEL)),
                ('is_credit_for', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.invoice')),
            ],
        ),
    ]