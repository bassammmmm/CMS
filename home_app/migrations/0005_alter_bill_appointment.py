# Generated by Django 4.1 on 2023-01-23 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0004_alter_bill_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home_app.appointment'),
        ),
    ]