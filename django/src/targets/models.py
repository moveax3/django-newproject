from django.db import models
from roles.models import Role
from model_utils.models import TimeStampedModel

class Target(TimeStampedModel):
    TARGET_TYPES = [
        (1, "Проект"),
        (2, "Навык"),
    ]
    target_type = models.PositiveIntegerField(
        verbose_name="Тип цели",
        choices=TARGET_TYPES,
        default=1,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        to              = "self",
        null            = True,
        blank           = True,
        verbose_name    = "Глобальная цель",
        on_delete       = models.CASCADE,
    )
    role = models.ForeignKey(
        to              = Role,
        blank           = False,
        null            = False,
        verbose_name    = "Роль",
        on_delete       = models.CASCADE,
    )
    title  = models.CharField(
        max_length      = 128,
        blank           = False,
        null            = False,
        verbose_name    = "Цель"
    )
    description = models.TextField(
        blank           = False,
        null            = False,
        verbose_name    = "Описание"
    )

    class Meta():
        verbose_name        = "Цель"
        verbose_name_plural = "Цели"

    def __str__(self):
        return self.title
