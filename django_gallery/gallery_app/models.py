from django.db import models

class Picture(models.Model):
    # change to picture type
    picture = models.CharField()
    # do I need this one ?
    name = models.CharField()
    # do I need this one ? change to bool if so
    grayscale = picture = models.CharField()