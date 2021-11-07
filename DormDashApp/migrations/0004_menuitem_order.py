# Generated by Django 3.2.8 on 2021-11-04 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DormDashApp', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='menuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resteraunt', models.CharField(max_length=100, null=True)),
                ('user', models.CharField(max_length=100, null=True)),
                ('items', models.ManyToManyField(to='DormDashApp.menuItem')),
            ],
        ),
    ]