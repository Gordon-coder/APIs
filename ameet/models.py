from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Competitor(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Throw(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    distance = models.FloatField()

    def __str__(self):
        return f"{self.competitor.name} at {self.event.name} - {self.distance}m"