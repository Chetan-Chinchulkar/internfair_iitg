# Generated by Django 3.1.2 on 2020-12-15 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internfair', '0002_auto_20201215_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startups',
            name='logo',
            field=models.ImageField(default='./startupLogo/default.png', upload_to='startupLogo'),
        ),
    ]
