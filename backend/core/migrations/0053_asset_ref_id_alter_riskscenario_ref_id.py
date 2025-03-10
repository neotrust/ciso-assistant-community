# Generated by Django 5.1.5 on 2025-02-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0052_securityexception_appliedcontrol_security_exceptions_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="asset",
            name="ref_id",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Reference ID"
            ),
        ),
        migrations.AlterField(
            model_name="riskscenario",
            name="ref_id",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Reference ID"
            ),
        ),
    ]
