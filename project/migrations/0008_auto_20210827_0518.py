# Generated by Django 3.2.6 on 2021-08-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_modeladmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='twitter',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='ModelAdmin',
        ),
    ]