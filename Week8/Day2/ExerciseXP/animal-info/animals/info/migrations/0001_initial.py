# Generated by Django 4.1.2 on 2022-10-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("legs", models.IntegerField()),
                ("weight", models.FloatField()),
                ("height", models.FloatField()),
                ("speed", models.IntegerField()),
                ("family", models.IntegerField()),
            ],
        ),
    ]
