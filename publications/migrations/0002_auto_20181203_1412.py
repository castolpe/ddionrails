# Generated by Django 2.1.3 on 2018-12-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("publications", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="publication", name="name", field=models.CharField(db_index=True, max_length=255)
        )
    ]