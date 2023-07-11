from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=130)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
        ordering = ["-id"]

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)



