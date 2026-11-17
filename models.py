from django.conf import settings
from django.db import models

class Natija(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="natijalar")
    wpm = models.FloatField()
    cpm = models.FloatField()
    aniqlik = models.FloatField()
    xatolar = models.PositiveIntegerField()
    togri = models.PositiveIntegerField()
    vaqt = models.PositiveIntegerField()
    seriya = models.JSONField(default=list)
    sana = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-sana"]
