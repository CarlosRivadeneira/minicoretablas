# Generated by Django 4.1.1 on 2023-01-25 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('minicore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='minicore.empresa'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]