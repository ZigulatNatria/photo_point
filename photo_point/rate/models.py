from django.db import models


class History(models.Model):
    history = models.JSONField()