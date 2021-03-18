from django.conf import settings
from django.db import models
from django.utils import timezone
 

class Zakaz(models.Model):
    nom_zak = models.IntegerField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    finish_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

