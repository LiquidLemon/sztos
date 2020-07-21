import datetime

from django.db import models
from django.utils import timezone


class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.text
