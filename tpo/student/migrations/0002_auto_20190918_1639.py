# Generated by Django 2.2.4 on 2019-09-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='m_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Middle Name'),
        ),
    ]
