# Generated by Django 4.0.4 on 2022-05-09 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='calories',
            field=models.IntegerField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='snack',
            name='gloten_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='snack',
            name='lactose_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='snack',
            name='sugar_free',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='snack',
            name='vegan',
            field=models.BooleanField(default=False),
        ),
    ]
