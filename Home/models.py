from django.db import models


# Create your models here.

class AxfWheel(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'


class AxfNav(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'


class AxfMustBuy(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'

class AxfMainShow(models.Model):
    img = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=128)

    img1 = models.CharField(max_length=128)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=128)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=128)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'
