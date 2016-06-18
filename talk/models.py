from django.db import models

class Post(models.Model):

    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __unicode__(self):
        return self.text
