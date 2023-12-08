from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category 
from .models.customer import Customer
from django.http import HttpResponse

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        password = postData.get('password')
        
        error_message = None

        if not first_name:
            error_message = "First Name is required."
        elif len(first_name) < 3:
            error_message = 'First Name must be 3 characters or more.'

        if not error_message:
            print(first_name, last_name, email, password)
            customer = Customer(first_name=first_name, last_name=last_name, email=email, password=password)
            customer.register()
        
            return HttpResponse("Signup Success")
        else:
            return render(request, 'signup.html', {'error': error_message})



def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            pass
        else:
            error_message ='Email or Password invalid '

