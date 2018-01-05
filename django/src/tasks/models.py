from django.db import models
from targets.models import Target
from model_utils.models import TimeStampedModel
from model_utils import Choices
from model_utils.fields import MonitorField, StatusField

class Task(TimeStampedModel):
    STATUS = Choices('Новая', 'В работе', 'Готово')
    status = StatusField()
    status_working_at = MonitorField(monitor='status', when=['В работе'])
    status_complete_at = MonitorField(monitor='status', when=['Готово'])

    parent = models.ForeignKey(
        to              = 'self',
        blank           = True,
        null            = True,
        verbose_name    = "Родительская задача",
        on_delete       = models.CASCADE,
        related_name    = '+',
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
    is_blocked  = models.ForeignKey(
        to              = 'self',
        blank           = True,
        null            = True,
        verbose_name    = "Блокируется",
        on_delete       = models.CASCADE,
        related_name    = '+',
    )

    class Meta():
        verbose_name        = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.title
