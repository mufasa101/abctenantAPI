# Generated by Django 3.2.5 on 2021-07-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20210714_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='property_auto',
            field=models.IntegerField(),
        ),
        migrations.AlterModelTable(
            name='property',
            table='property',
        ),
        migrations.DeleteModel(
            name='Property_new',
        ),
    ]
