from django.db import models

# Create your models here.



class temphum(models.Model):
    temperature = models.DecimalField(max_digits=20, decimal_places=10)
    humidity = models.DecimalField(max_digits=20, decimal_places=10)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return str(self.temperature)

class Status(models.Model):
    Status = models.BooleanField()
