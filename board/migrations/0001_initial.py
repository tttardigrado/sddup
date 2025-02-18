# Generated by Django 4.1.13 on 2024-08-13 13:11

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoardPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                (
                    "board",
                    wagtail.fields.StreamField(
                        [
                            (
                                "board",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "name",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Nome"
                                            ),
                                        ),
                                        (
                                            "position",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Cargo"
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True, verbose_name="Fotografia"
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=False,
                        verbose_name="Direção",
                    ),
                ),
                (
                    "general_assembly",
                    wagtail.fields.StreamField(
                        [
                            (
                                "general_assembly",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "name",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Nome"
                                            ),
                                        ),
                                        (
                                            "position",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Cargo"
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True, verbose_name="Fotografia"
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=False,
                        verbose_name="Mesa da Assembleia Geral",
                    ),
                ),
                (
                    "auditing",
                    wagtail.fields.StreamField(
                        [
                            (
                                "auditing",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "name",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Nome"
                                            ),
                                        ),
                                        (
                                            "position",
                                            wagtail.blocks.CharBlock(
                                                required=True, verbose_name="Cargo"
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=True, verbose_name="Fotografia"
                                            ),
                                        ),
                                    ]
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                        use_json_field=False,
                        verbose_name="Conselho Fiscal",
                    ),
                ),
            ],
            options={
                "verbose_name": "Orgãos Sociais",
                "verbose_name_plural": "Mandatos",
            },
            bases=("wagtailcore.page",),
        ),
    ]
