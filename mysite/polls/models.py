from django.db import models

# Each model has a number of class variables, each of which represents a database field in the model.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# First we need to tell our project that the polls app is installed.
# Edit the mysite/settings.py file and add that dotted path to the INSTALLED_APPS setting.