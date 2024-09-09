# Generated by Django 4.1.13 on 2024-08-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("snippets", "0008_alter_contact_options_contact_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Nome do Evento"),
                ),
                (
                    "location",
                    models.CharField(max_length=100, verbose_name="Local do Evento"),
                ),
                ("start_date", models.DateField(verbose_name="Data de Início")),
                ("end_date", models.DateField(verbose_name="Data de Fim")),
                (
                    "hour",
                    models.TimeField(blank=True, null=True, verbose_name="Horário"),
                ),
                ("url", models.URLField(verbose_name="Link")),
            ],
            options={
                "verbose_name": "Evento",
                "verbose_name_plural": "Eventos",
                "ordering": ["start_date", "name"],
            },
        ),
    ]
