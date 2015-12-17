from django.db import models

# Create your models here.


class Side(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Faction(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Operator(models.Model):
    faction = models.ForeignKey(Faction)
    side = models.ForeignKey(Side)
    name = models.CharField(max_length=200)
    armor = models.IntegerField()
    speed = models.IntegerField()
    portrait = models.CharField(max_length=500, null=True)
    logo = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Gadget(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=250)
    passcode = models.IntegerField()

    def __str__(self):
        return self.name
