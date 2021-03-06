from django.db import models

# Create your models here.

class AxfFoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=256)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'


class AxfGoods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=128)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=128)

    isxf = models.BooleanField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=16)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=64)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'
