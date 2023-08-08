from django.db import models

# Create your models here.

class ListNews(models.Model):
    name_st = models.CharField(max_length=300, unique=True)
    text_st = models.TextField()
    data_cr_st = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_st