from django.db import models


class Note(models.Model):
    note_title = models.CharField(max_length=200)
    note_text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Create your models here.
