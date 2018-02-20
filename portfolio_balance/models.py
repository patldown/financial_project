from django.db import models

# Create your models here.

class Question(models.Model):
    ### Each of the below variables represent a field based on
    ### --- models.Model subclass. Field classes are used...
    ### --- e.g. CharField/DateTimeField
    question_text = models.CharField(max_length=200)
    ### notice we provided a human readable fieldname or 'date published',
    ### --- This is optional
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    ### Models.Foreign_Key defines a relationship as in each choice is related
    ### --- to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)