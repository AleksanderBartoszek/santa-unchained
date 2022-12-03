# Generated by Django 4.1.3 on 2022-12-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wishes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "New"),
                    ("ACCEPTED", "Accepted"),
                    ("REJECTED", "Rejected"),
                    ("READY_FOR_SHIPPING", "Ready for shipping"),
                    ("DELIVERED", "Delivered"),
                ],
                default="NEW",
                max_length=18,
            ),
        ),
    ]
