# Generated by Django 5.0.3 on 2024-05-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_alter_pembayaran_metode'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembayaran',
            name='nomor_wa',
            field=models.CharField(default='+62', max_length=16),
        ),
    ]
