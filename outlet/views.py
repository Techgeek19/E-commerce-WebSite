from django.shortcuts import render, HttpResponse
from django.contrib import messages
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json

# Create your views here.


# def index(request):
#     obj= Product.objects.all()
#     return render(request,'outlet/a.html',{'obj':obj})



def index(request):
    # # obj= Product.objects.all()
    # # allprod= [[obj],[obj]]
    allprod= []
    cat_prod = Product.objects.values('category', 'id')
    #.values returns dictionaries 
    # OUTPUT[{'category': 'test', 'id': 1}, {'category': 'testing', 'id': 2}, {'category': 'test 3', 'id': 3}, {'category': 'test 4 cat', 'id': 4}, {'category': 'test 5', 'id': 5}, {'category': 'test', 'id': 6}]
    cat_items= { item['category'] for item in cat_prod}
    # output {'testing', 'test', 'test 4 cat', 'test 3', 'test 5'} <-- Category Items
    for c in cat_items:
        prod= Product.objects.filter(category= c) 
        #categorywise Filter
        allprod.append([prod])
    #     allProds.append([prod, range(1, nSlides), nSlides])
    # params = {'allProds':allProds}
    return render(request,'outlet/index.html',{'allprod':allprod})

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprod= []
    cat_prod = Product.objects.values('category', 'id')
    cat_items= { item['category'] for item in cat_prod}
    for c in cat_items:
        prodtemp= Product.objects.filter(category= c) 
        prod = [item for item in prodtemp if searchMatch(query, item)]
        #categorywise Filter
        if len(prod) != 0:
            allprod.append([prod])
    params = {'allprod': allprod, "msg": ""}
    if len(allprod) == 0 or len(query)<3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request,'outlet/search.html', params)


def about(request):
    return render(request,'outlet/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        messages.info(request, 'Thanks for connecting with us. Your message has been successfully delivered')
    return render(request,'outlet/contact.html', {})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'outlet/tracker.html')



def prodview(request, id):
    #fetching product using id
    obj= Product.objects.filter(id=id)
    print(obj[0])
    return render(request,'outlet/prodview.html', {'obj':obj[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        messages.info(request, 'Thanks for ordering with us.')
        id = order.order_id
        return render(request, 'outlet/checkout.html', {'id': id})
    return render(request,'outlet/checkout.html', {})

    
