# Generated by Django 4.2.6 on 2024-01-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card',
            field=models.DateField(auto_now_add=True),
        ),
    ]
