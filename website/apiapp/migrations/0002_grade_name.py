# Generated by Django 4.0.1 on 2022-02-10 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='name',
            field=models.CharField(default='grade', max_length=10),
        ),
    ]
