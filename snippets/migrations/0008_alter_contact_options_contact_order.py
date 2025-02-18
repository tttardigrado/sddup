# Generated by Django 4.1.13 on 2024-08-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0007_alter_contact_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={
                "ordering": ["order", "title", "kind", "text"],
                "verbose_name": "contacto",
                "verbose_name_plural": "contactos",
            },
        ),
        migrations.AddField(
            model_name="contact",
            name="order",
            field=models.IntegerField(default=0, verbose_name="Ordem"),
        ),
    ]
