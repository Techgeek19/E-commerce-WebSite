from django.shortcuts import render, HttpResponse
from .models import Product, Contact

# Create your views here.
def index(request):
    # obj= Product.objects.all()
    # allprod= [[obj],[obj]]
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
    return render(request,'outlet/index.html', {'allprod': allprod})

def about(request):
    return render(request,'outlet/about.html')

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, email=email, message=message)
        contact.save()
    return render(request,'outlet/contact.html', {})

def tracker(request):
    return render(request,'outlet/tracker.html', {})

def search(request):
    return render(request,'outlet/search.html', {})

def prodview(request, id):
    #fetching product using id
    obj= Product.objects.filter(id=id)
    print(obj[0])
    return render(request,'outlet/prodview.html', {'obj':obj[0]})

def checkout(request):
    return render(request,'outlet/checkout.html', {})

    