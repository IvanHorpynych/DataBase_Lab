from __future__ import unicode_literals

from xml.dom import minidom

from django.db import models
from django.db.models import Manager


class ProductManager(models.Manager):
    def initialize(self,):
        self.model.objects.all().delete()
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE sales_product AUTO_INCREMENT = 1")
        xmldoc = minidom.parse('tables.xml')
        product_list = xmldoc.getElementsByTagName('product')
        for product in product_list:
            productName = str(product.getElementsByTagName('productName')[0].firstChild.data)
            productPrice = int(product.getElementsByTagName('productPrice')[0].firstChild.data)
            self.model.objects.create(productName=productName, productPrice=productPrice)


class UserManager(models.Manager):
    def initialize(self,):
        self.model.objects.all().delete()
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE sales_user AUTO_INCREMENT = 1")
        xmldoc = minidom.parse('tables.xml')
        product_list = xmldoc.getElementsByTagName('user')
        for product in product_list:
            userName = str(product.getElementsByTagName('userName')[0].firstChild.data)
            userSurname = str(product.getElementsByTagName('userSurname')[0].firstChild.data)
            userAge = int(product.getElementsByTagName('userAge')[0].firstChild.data)
            self.model.objects.create(userName=userName, userSurname=userSurname, userAge=userAge)



class DepartmentManager(models.Manager):
    def initialize(self,):
        self.model.objects.all().delete()
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("ALTER TABLE sales_department AUTO_INCREMENT = 1")
        xmldoc = minidom.parse('tables.xml')
        product_list = xmldoc.getElementsByTagName('department')
        for product in product_list:
            depName = str(product.getElementsByTagName('departmentName')[0].firstChild.data)
            depAdd = str(product.getElementsByTagName('departmentAddress')[0].firstChild.data)
            self.model.objects.create(departmentName=depName, departmentAddress=depAdd)





class User(models.Model):
    userName = models.CharField(max_length=50)
    userSurname = models.CharField(max_length=50)
    userAge = models.IntegerField()
    objects = UserManager()


class Department(models.Model):
    departmentName = models.CharField(max_length=50)
    departmentAddress = models.CharField(max_length=50)
    objects = DepartmentManager()


class Product(models.Model):
    productName = models.CharField(max_length=50)
    productPrice = models.IntegerField()
    objects = ProductManager()



class Sales(models.Model):
    user = models.ForeignKey(User)
    department = models.ForeignKey(Department)
    product = models.ForeignKey(Product)
    saleType = models.CharField(max_length=50)
    saleDescription = models.CharField(max_length=50)
    objects = Manager()

# Create your models here.

