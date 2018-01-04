from django.db import models
from targets.models import Target
from model_utils.models import TimeStampedModel

class Task(TimeStampedModel):
    parent = models.ForeignKey(
        to              = 'self',
        blank           = True,
        null            = True,
        verbose_name    = "Родительская задача",
        on_delete       = models.CASCADE
    )
    target = models.ForeignKey(
        to              = Target,
        blank           = False,
        null            = False,
        verbose_name    = "Цель",
        on_delete       = models.CASCADE
    )
    title  = models.CharField(
        max_length      = 128,
        blank           = False,
        null            = False,
        verbose_name    = "Задача"
    )
    description = models.TextField(
        blank           = False,
        null            = False,
        verbose_name    = "Описание"
    )

    class Meta():
        verbose_name        = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
