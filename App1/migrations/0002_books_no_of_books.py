# Generated by Django 4.0.5 on 2022-06-10 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='No_of_books',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
