from django.db import models
from django.utils import timezone

class Message(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        return self.text

