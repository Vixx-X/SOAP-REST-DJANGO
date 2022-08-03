# Generated by Django 4.0.1 on 2022-08-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("name", models.CharField(max_length=255, verbose_name="Task name")),
                ("description", models.TextField(verbose_name="Task description")),
                (
                    "importance",
                    models.CharField(
                        choices=[
                            ("Low", "Low importance"),
                            ("Mid", "Mid importance"),
                            ("High", "High importance"),
                        ],
                        default="Mid",
                        max_length=32,
                    ),
                ),
                (
                    "marked",
                    models.BooleanField(
                        db_index=True,
                        default=False,
                        help_text="Check this task if is not longer todo",
                        verbose_name="Task is completed",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="Date created"
                    ),
                ),
                (
                    "date_completed",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="Date completed"
                    ),
                ),
            ],
            options={
                "verbose_name": "Task",
                "verbose_name_plural": "Tasks",
                "db_table": "tasks",
            },
        ),
    ]