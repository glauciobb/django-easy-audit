# Generated by Django 2.1 on 2019-07-23 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyaudit', '0012_auto_20181018_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestevent',
            name='url',
            field=models.CharField(db_index=True, max_length=254),
        ),
    ]
