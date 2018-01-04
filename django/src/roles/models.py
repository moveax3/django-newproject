from django.db import models
from model_utils.models import TimeStampedModel

class Role(TimeStampedModel):
    title  = models.CharField(
        max_length      = 128,
        blank           = False,
        null            = False,
        verbose_name    = "Название"
    )

    class Meta():
        verbose_name        = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.title
