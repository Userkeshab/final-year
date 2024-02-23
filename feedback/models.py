from django.db import models

# Create your models here.
class Feedback(models.Model):
    feedback = models.CharField(max_length=1050, null=True)

