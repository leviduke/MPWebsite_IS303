from django.db import models

# Create your models here.
class Place (models.Model) :
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)


    def __str__(self) :
        return (self.city)

class Person (models.Model) :
    date_missing = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age_when_missing = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    race = models.CharField(max_length=20)
    place = models.ManyToManyField(Place, blank=True)

    def __str__(self) :
        return (self.full_name)
    
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(Person, self).save()
    
