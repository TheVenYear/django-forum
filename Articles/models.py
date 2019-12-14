from django.db import models
from django.core.validators import RegexValidator

class Rubric(models.Model):
    alphanumeric = RegexValidator(regex = '[a0-9-zA-Z]*$', message = 'Только латинские буквы')
    name = models.CharField(max_length = 50)
    url = models.CharField(max_length = 15, validators = [alphanumeric])
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True, db_index = True)
    rubric = models.ForeignKey(Rubric, on_delete = models.PROTECT, default = None)
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    commentator = models.CharField(max_length = 20)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True, db_index = True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE, default = None)
    def __str__(self):
        return self.commentator 
