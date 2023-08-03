# Generated by Django 3.2.20 on 2023-08-03 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=10, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regin_area', to='mediciones.area')),
            ],
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(default=0)),
                ('humidity', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('note', models.TextField(blank=True, null=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='mediciones.region')),
            ],
        ),
    ]