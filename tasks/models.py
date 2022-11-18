from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):

    class Status(models.TextChoices):
        UNASSIGNED = 'UN', 'Unassigned'
        INPROGRESS = 'IP', 'In Progress'
        CLOSED = 'CL', 'Closed'

    class Status(models.TextChoices):
        HIGH = 'HI', 'High'
        MEDIUM = 'MD', 'Medium'
        LOW = 'LO', 'LOW'

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description =  models.TextField()
    creator = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.UNASSIGNED)
    priority = models.CharField(max_length=2,
                                choices=Status.choices,
                                default=Status.LOW)
    assigned_to = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['-priority']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title