# Generated by Django 3.1.7 on 2021-09-26 04:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BakeryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('PCS', 'Pieces'), ('KG', 'Kilogram'), ('GM', 'Gram'), ('Dozen', 'Dozen'), ('LTR', 'Litre')], max_length=20)),
                ('cost_price', models.FloatField(blank=True, null=True)),
                ('sell_price', models.FloatField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bak_cr_d', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bak_up_d', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('desc', models.TextField(blank=True)),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, choices=[('PCS', 'Pieces'), ('KG', 'Kilogram'), ('GM', 'Gram'), ('Dozen', 'Dozen'), ('LTR', 'Litre')], max_length=20)),
                ('per_unit_in_kg', models.FloatField(blank=True, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ing_cr_d', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ing_up_d', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IngItemMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_kg', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bakery_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery_admin.bakeryitem')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingbak_cr_d', to=settings.AUTH_USER_MODEL)),
                ('ing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bakery_admin.ingredient')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingbak_up_d', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]