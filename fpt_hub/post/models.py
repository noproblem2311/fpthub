from venv import create
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    class Meta:
        ordering = ['id']
    image=models.ImageField(upload_to='uploads/%Y/%m')
    flags=models.CharField(max_length=200)
    seeds=models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    topic= models.ManyToManyField('Topic', related_name='topic')

    def __str__(self):
        return self.content
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



# class ActionBase(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now_add=True)
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

#     class Meta:
#         abstract = True
# class Action(ActionBase):
#     FLAG, SEED = range(2)
#     ACTIONS=[
#         (FLAG,'flag'),
#         (SEED,'seed'),
#     ]
#     type=models.PositiveSmallIntegerField(choices=ACTIONS, default=FLAG)