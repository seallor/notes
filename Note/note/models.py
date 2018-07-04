from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    unique_words = models.IntegerField(default=0)

    def publish(self):
        self.unique_words = len(set((''.join(x for x in str(self.text) if x not in '-.:;!@#$%^&}{[]><\|`~*()_+=-"?/,')
                                     ).lower().split(" ")) - {''})
        self.save()

    def __str__(self):
        return self.title


# Create your models here.
