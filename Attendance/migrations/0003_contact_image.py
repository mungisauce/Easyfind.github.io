# Generated by Django 5.1.3 on 2024-12-06 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Attendance', '0002_contact_delete_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='image',
            field=models.ImageField(blank=True, upload_to='radicalConnect_images/'),
        ),
    ]
