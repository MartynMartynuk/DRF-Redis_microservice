# Generated by Django 4.0.3 on 2022-04-01 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endpoint_field', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('dev_type', models.CharField(max_length=7)),
                ('dev_id', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('endpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='microservice.endpoints')),
            ],
        ),
    ]
