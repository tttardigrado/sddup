# Generated by Django 4.1.13 on 2024-08-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0004_alter_sponsor_options_alter_contact_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="show_in_footer",
            field=models.BooleanField(default=True, verbose_name="Mostrar no Footer"),
        ),
    ]
