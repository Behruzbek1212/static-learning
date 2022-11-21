from django.db import models

class Car(models.Model):
    position = models.CharField(max_length=20)
    content = models.TextField()
    price = models.IntegerField()
    picture = models.CharField(max_length=255)

    def __str__(self):
        return self.position