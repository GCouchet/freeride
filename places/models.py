from django.db import models


class Country(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name    


class City(models.Model):
    name = models.CharField(unique=True, max_length=30, blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=40, blank=False)
    image = models.ImageField(blank=True, null=True, verbose_name="Image")
    description = models.TextField(max_length=255, blank=True, null=True, default="")
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL, related_name="country")
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL, related_name="city")

    class Meta:
        unique_together = ['country', 'city', 'name']

    def __str__(self):
        return self.name  
    