# Generated by Django 3.2.6 on 2021-08-26 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_about_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelAdmin',
            fields=[
                ('about_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='project.about')),
            ],
            bases=('project.about',),
        ),
    ]