"""
Models for todo app
"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):

    name = models.CharField(
        _("Task name"),
        max_length=255,
    )

    description = models.TextField(
        _("Task description"),
    )

    LOW, MID, HIGH, = (
        "Low",
        "Mid",
        "High",
    )
    importance_choices = (
        (LOW, _("Low importance")),
        (MID, _("Mid importance")),
        (HIGH, _("High importance")),
    )
    importance = models.CharField(
        max_length=32,
        choices=importance_choices,
        default=MID,
    )

    marked = models.BooleanField(
        _("Task is completed"),
        help_text=_("Check this task if is not longer todo"),
        db_index=True,
        default=False,
    )

    date_created = models.DateTimeField(
        _("Date created"),
        auto_now_add=True,
        db_index=True,
    )

    date_completed = models.DateTimeField(
        _("Date completed"),
        blank=True,
        null=True,
    )

    class Meta:
        app_label = "todo"
        db_table = "tasks"
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return f"Task #{self.id} - {self.name}"
