# Generated by Django 3.2.3 on 2021-05-31 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='profile-pictures/default.png', upload_to='profile-pictures/'),
        ),
    ]