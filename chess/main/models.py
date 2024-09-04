from django.db import models


class Players(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    rank = models.CharField(max_length=30, default='Novices')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Players"
        verbose_name = "Player"
        ordering = ["age"]

