# Generated by Django 3.1.5 on 2021-12-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeration',
            name='Mobile',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='registeration',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
