from xml.dom import minidom
import MySQLdb as mdb
import sys


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

    def initialization(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)

        cur.execute("DELETE FROM sales")
        cur.execute("ALTER TABLE sales AUTO_INCREMENT = 1")
        cur.execute("commit")

        cur.execute("DELETE FROM user ")
        cur.execute("ALTER TABLE user AUTO_INCREMENT = 1")
        cur.execute("commit")

        cur.execute("DELETE FROM product")
        cur.execute("ALTER TABLE product AUTO_INCREMENT = 1")
        cur.execute("commit")

        cur.execute("DELETE FROM department")
        cur.execute("ALTER TABLE department AUTO_INCREMENT = 1")
        cur.execute("commit")



        xmldoc = minidom.parse('tables.xml')

        user_list = xmldoc.getElementsByTagName('user')
        for user in user_list:
            userName = str(user.getElementsByTagName('userName')[0].firstChild.data)
            userSurname = str(user.getElementsByTagName('userSurname')[0].firstChild.data)
            userAge = int(user.getElementsByTagName('userAge')[0].firstChild.data)
            cur.execute("INSERT INTO user (userName, userSurname, userAge) VALUES('%s', '%s', '%d')" %
                        (userName, userSurname, userAge,))
            cur.execute("commit")
            print(userName, userSurname, userAge)

        product_list = xmldoc.getElementsByTagName('product')
        for product in product_list:
            productName = str(product.getElementsByTagName('productName')[0].firstChild.data)
            productPrice = int(product.getElementsByTagName('productPrice')[0].firstChild.data)
            cur.execute("INSERT INTO product (productName, productPrice) VALUES('%s', '%d')" %
                        (productName, productPrice,))
            cur.execute("commit")
            print(productName, productPrice)

        department_list = xmldoc.getElementsByTagName('department')
        for department in department_list:
            departmentName = str(department.getElementsByTagName('departmentName')[0].firstChild.data)
            departmentAddress = str(department.getElementsByTagName('departmentAddress')[0].firstChild.data)
            cur.execute("INSERT INTO department (departmentName, departmentAddress) VALUES('%s', '%s')" %
                        (departmentName, departmentAddress))
            cur.execute("commit")
            print(departmentName, departmentAddress)

        sales_list = xmldoc.getElementsByTagName('sale')
        for sale in sales_list:
            userId = int(sale.getElementsByTagName('userId')[0].firstChild.data)
            productId = int(sale.getElementsByTagName('productId')[0].firstChild.data)
            departmentId = int(sale.getElementsByTagName('departmentId')[0].firstChild.data)
            saleType = str(sale.getElementsByTagName('saleType')[0].firstChild.data)
            saleDate = str(sale.getElementsByTagName('saleDescription')[0].firstChild.data)
            cur.execute(
                "INSERT INTO sales (user, product, department, saleType, saleDescription) VALUES('%d', '%d', '%d', '%s', '%s')" %
                (userId, productId, departmentId, saleType,saleDate))
            cur.execute("commit")
        self.close()

    def getSalesList(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM sales, user, product, department WHERE sales.product=product.productId "
            "AND sales.user=user.userId "
            "AND sales.department=department.departmentId")
        self.close()
        return cur.fetchall()

    def getSale(self, id):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM sales, user, product, department WHERE sales.product=product.productId "
            "AND sales.user=user.userId "
            "AND sales.department=department.departmentId "
            "AND sales.salesId=%d" % int(id))
        self.close()
        return cur.fetchone()

    def getUsers(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM user")
        self.close()
        return cur.fetchall()

    def getDepartments(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM department")
        self.close()
        return cur.fetchall()

    def getProducts(self):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM product")
        self.close()
        return cur.fetchall()

    def saveSale(self,userid,productId,departmentId,saleType,saleDescription):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("INSERT INTO sales (user, product, department, saleType, saleDescription)"
                    " VALUES('%d', '%d', '%d', '%s', '%s')" %
        (int(userid), int(productId), int(departmentId), saleType, saleDescription))
        cur.execute("commit")
        self.close()

    def updateSale(self,saleid,userid,productId,departmentId,saleType,saleDescription):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("UPDATE sales SET user='%d', product='%d', "
                    "department='%d', saleType='%s', saleDescription='%s' where salesId=%d" %
        (int(userid), int(productId), int(departmentId), saleType, saleDescription,int(saleid) ))
        cur.execute("commit")
        self.close()

    def removeSale(self, id):
        self.connect()
        if self.connection is None:
            return []
        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute("DELETE FROM sales WHERE salesId = '%d' " % (int(id)))
        cur.execute("commit")
        self.close()


    def getSalesListByAge(self, fromAge, toAge):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM sales, user, product, department WHERE sales.product=product.productId "
            "AND sales.user=user.userId "
            "AND sales.department=department.departmentId "
            "AND user.userAge BETWEEN '%d'  AND  '%d'  " %(fromAge, toAge))

        self.close()
        return cur.fetchall()


    def getSalesListByDepartmentID(self, depID):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)
        cur.execute(
            "SELECT * FROM sales, user, product, department WHERE sales.product=product.productId "
            "AND sales.user=user.userId "
            "AND sales.department=department.departmentId "
            "AND sales.department = '%d' " % depID )
        self.close()
        return cur.fetchall()
    def getListExcluded(self, phrase):
        self.connect()
        if self.connection is None:
            return []

        cur = self.connection.cursor(mdb.cursors.DictCursor)

        cur.execute("SELECT * FROM sales, product, user, department WHERE "
                    "(MATCH (sales.saleDescription) AGAINST ( '-%s' IN BOOLEAN MODE) "
                    "AND sales.user = user.userId "
                    "AND sales.product = product.productId "
                    "AND sales.department = department.departmentId)" % phrase)
        self.close()
        return cur.fetchall()
