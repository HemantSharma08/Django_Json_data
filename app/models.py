from django.db import models


class Data(models.Model):
    id = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=500, null=True, blank=True)
    topic = models.CharField(max_length=100, null=True, blank=True)
    insight = models.TextField(null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.title  # Or any other field you want to display
