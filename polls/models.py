from django.utils import timezone
import datetime
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date puplished')

    def __unicode__ (self):  # __str__ on Python 3
        return self.question_text

    def was_publiched_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__ (self):  # __str__ on Python 3
        return self.choice_text