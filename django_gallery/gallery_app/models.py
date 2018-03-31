from django.db import models

class Picture(models.Model):
    # change to picture type
    #picture = models.CharField(max_length=100)
    # do I need this one ?
    name = models.CharField(max_length=100)
    isGrayscaled = models.BooleanField(default=False)
    # do I need this one ? change to bool if so
    #grayscale = models.CharField(max_length=100)