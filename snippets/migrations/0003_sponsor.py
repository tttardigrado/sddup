# Generated by Django 4.1.13 on 2024-08-14 08:35

from django.db import migrations, models
import django.db.models.deletion
import wagtail.models


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("snippets", "0002_alter_contact_kind"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sponsor",
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
                    models.CharField(
                        max_length=255, verbose_name="Nome do Patrocinador"
                    ),
                ),
                (
                    "logo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                        verbose_name="Logo do Patrocinador",
                    ),
                ),
            ],
            options={
                "verbose_name": "contacto",
                "verbose_name_plural": "contactos",
                "ordering": ["name"],
            },
            bases=(wagtail.models.PreviewableMixin, models.Model),
        ),
    ]
