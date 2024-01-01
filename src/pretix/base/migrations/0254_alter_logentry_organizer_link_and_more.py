# Generated by Django 4.2.4 on 2023-12-06 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pretixbase", "0253_checkin_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="organizer_link",
            field=models.ForeignKey(
                db_column="organizer_link_id",
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="pretixbase.organizer",
            ),
        ),
        migrations.RenameField(
            model_name="logentry",
            old_name="organizer_link",
            new_name="organizer",
        ),
    ]