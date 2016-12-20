from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Database import DB


# Create your views here.


def index(request):
    return render(request, 'adminpage.html',{'message':request.GET.get('message',None)})


def initializeDatabase(request):
    database = DB()
    database.initialization()
    return redirect(reverse('index')+ '?message=Database initialized')


def listView(request):
    database = DB()

    if 'fromAge' in request.GET and 'toAge' in request.GET:
        list = database.getSalesListByAge(int(request.GET['fromAge']), int(request.GET['toAge']))

    elif 'departmentId' in request.GET:
        list = database.getSalesListByDepartmentID(int(request.GET['departmentId']))
    elif 'excludeWord' in request.GET:
        list = database.getListExcluded(request.GET['excludeWord'])
    elif 'containsString' in request.GET:
        list = database.getListExcluded(request.GET['containsString'])
    else:
        list = database.getSalesList()
    departments = database.getDepartments()
    return render(request,'listpage.html',{'list':list, 'departments':departments})


def removeSale(request, id):
    database = DB()
    database.removeSale(id)
    return redirect(reverse('index') + '?message=Removed record')


def editSale(request, id):
    database = DB()
    if request.method == 'GET':
        customers = database.getUsers()
        departments = database.getDepartments()
        products = database.getProducts()
        sale = database.getSale(id)
        print sale
        return render(request,'editSale.html', {'customers':customers, 'departments':departments, 'products':products, 'sale': sale })
    else:
        database.updateSale(id, request.POST['userId'],request.POST['productId'],request.POST['departmentId'],
                  request.POST['saleType'],request.POST['saleDescription'])
        return redirect(reverse('index') + '?message=Changed Sale')



def addSale(request):
    database = DB()
    if request.method == 'GET':
        customers = database.getUsers()
        departments = database.getDepartments()
        products = database.getProducts()
        return render(request,'addSale.html', {'customers':customers, 'departments':departments, 'products':products})
    elif request.method == 'POST':
        database.saveSale(request.POST['userId'],request.POST['productId'],request.POST['departmentId'],
                          request.POST['saleType'],request.POST['saleDescription'])
        return redirect(reverse('index') + '?message=Added Sale')

