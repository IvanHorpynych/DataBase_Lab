from xml.dom import minidom
import MySQLdb as mdb
import sys

from models import Sales, Department, User, Product


class DB(object):
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is not None:
            return
        try:
            self.connection = mdb.connect('localhost','root','root','pythonlab')

        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            self.connection = None

    def close(self):
        if self.connection is not None:
            self.connection.close()
        self.connection = None


    def enableTrigger(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("CREATE TRIGGER backuper "
                    "AFTER DELETE ON sales_sales "
                    "for each row "
                    "CALL logSale()" )
        self.close()

    def disableTrigger(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DROP trigger backuper;")
        self.close()

    def setEventTime(self, time):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("ALTER EVENT clearEvent ON SCHEDULE EVERY %s MINUTE" % time)
        self.close()

    def getSalesList(self):
        return Sales.objects.all()

    def getSale(self, id):
        return Sales.objects.get(id=id)

    def getUsers(self):
        return User.objects.all()

    def getDepartments(self):
        return Department.objects.all()

    def getProducts(self):
        return Product.objects.all()

    def saveSale(self,userid,productId,departmentId,saleType,saleDescription):
        user = User.objects.get(id=int(userid))
        product = Product.objects.get(id=int(productId))
        department = Department.objects.get(id=int(departmentId))
        Sales.objects.create(user=user,product=product,department=department,saleType=saleType,saleDescription=saleDescription)


    def updateSale(self,saleid,userid,productId,departmentId,saleType,saleDescription):
        sale = Sales.objects.get(id=saleid)
        user = User.objects.get(id=userid)
        product = Product.objects.get(id=productId)
        department = Department.objects.get(id=departmentId)
        sale.user = user
        sale.product = product
        sale.department = department
        sale.saleType = saleType
        sale.saleDescription = saleDescription
        sale.save()

    def removeSale(self, id):
        Sales.objects.get(id=int(id)).delete()

    def getSalesListByAge(self, fromAge, toAge):
        sales = Sales.objects.filter(user__userAge__range=[int(fromAge),int(toAge)])
        return sales

    def getSalesListByDepartmentID(self, depID):
        dep = Department.objects.get(id=depID)
        sales = Sales.objects.filter(department=dep)
        return sales


    def getListExcluded(self, phrase):
        return Sales.objects.exclude(saleDescription__contains=phrase)


    def getListContains(self, phrase):
        return Sales.objects.filter(saleDescription__contains=phrase)


