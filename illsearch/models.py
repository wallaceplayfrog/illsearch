from django.db import models

# Create your models here.


class Info(models.Model):

    num = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    age = models.CharField(max_length=3)
    section = models.CharField(max_length=5)
    time = models.CharField(max_length=20)

    class Meta:
        db_table = 'info'


class Complain(models.Model):

    num = models.IntegerField(primary_key=True)
    word1 = models.CharField(max_length=7, blank=True, default='')
    word2 = models.CharField(max_length=7, blank=True, default='')
    word3 = models.CharField(max_length=7, blank=True, default='')

    class Meta:
        db_table = 'complain'


class Diagnose(models.Model):

    num = models.IntegerField(primary_key=True)
    ill1 = models.CharField(max_length=10, blank=True, default='')
    ill2 = models.CharField(max_length=10, blank=True, default='')
    ill3 = models.CharField(max_length=10, blank=True, default='')
    ill4 = models.CharField(max_length=10, blank=True, default='')
    ill5 = models.CharField(max_length=10, blank=True, default='')

    class Meta:
        db_table = 'diagnose'


class Dispose(models.Model):

    num = models.IntegerField(primary_key=True)
    med1 = models.CharField(max_length=30, blank=True, default='')
    med2 = models.CharField(max_length=30, blank=True, default='')
    med3 = models.CharField(max_length=30, blank=True, default='')
    med4 = models.CharField(max_length=30, blank=True, default='')
    med5 = models.CharField(max_length=30, blank=True, default='')
    med6 = models.CharField(max_length=30, blank=True, default='')

    class Meta:
        db_table = 'dispose'

