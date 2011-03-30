from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name