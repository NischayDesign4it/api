# Generated by Django 4.2.13 on 2024-05-23 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dht', '0005_alter_temphum_humidity_alter_temphum_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='pdf_files/')),
            ],
        ),
    ]
