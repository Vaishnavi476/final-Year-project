from app.forms import FeedbackForm
from app.forms import ProfileForm, ServiceRequestForm
from typing import ContextManager
from django.shortcuts import render, redirect
from .models import  Human_Resource, Profile, Purchase, ServiceRequest, Contact, EquipmentRental
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from app.forms import PurchaseForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import Equipment
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe



# Create your views here.
def homeview(request):
    ctx ={'title':'welcome'}
    return render(request,'index.html',context= ctx)

def welcomeview(request):
    return render(request,'welcome.html')

def ordering(request):
    return render(request,'ordering.html')

def view_hr(request):
    hr = Human_Resource.objects.all() 
    context = {'hr':hr}       
    return render(request,'hr/view.html',context)

def detail_hr(request,pk):
    hr= Human_Resource.objects.get(pk=pk)
    context = {'hr':hr}
    return render(request,'hr/detail.html',context)

def index(request):
    return render(request, 'index.html')
 
def purchase(request):
    equipments = Equipment.objects.all()
    context = {'equipments':equipments}       
    return render(request,'purchase/purchase.html',context)

def feedback(request):
    form = FeedbackForm()
    if request.method=='POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your feedback is sent to admin')
            return redirect("feedback")
    ctx={'title':'feedback','form':form}
    return render(request,'feedback.html',ctx)


def show_products(request):
    products = Equipment.objects.all()
    ctx = {'products':products}
    return render(request,'store/product_view.html',ctx)

def show_single_product(request,pk):
    product = get_object_or_404(Equipment,pk=pk)
    ctx = {'product':product}
    return render(request,'store/product_detail.html',ctx)

@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Equipment.objects.get(id=id)
    cart.add(product=product)
    return redirect("product_all")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Equipment.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Equipment.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Equipment.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')

@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {'publicKey':settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config,safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method =='GET':
        domain_url = "http://127.0.0.1:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # product data
            checkout_session = stripe.checkout.Session.create(
                success_url = domain_url+'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url = domain_url+'cancelled/',
                payment_method_types = ['card'],
                mode = 'payment',
                line_items = [{
                    'name':'ABCD',
                    'quantity':5,
                    'currency':'inr',
                    'amount':200020, # Rs  2000 and 20 paise 
                }] 
            )
            cart = Cart(request)
            cart.clear()
            return JsonResponse({'sessionId':checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error':str(e)})

def notify_success(request):
    messages.success(request,f"Your payment is complete.")
    return redirect('home')

def notify_cancelled(request):
    messages.error(request,f"Your payment is cancelled.")
    return redirect('cart_detail')

def rent(request):
    equipment = EquipmentRental.objects.all()
    ctx = {"eqiupmentrental":equipment}
    return render(request,'rent_services/rent.html',ctx)

def equipment(request):
    equipment = Equipment.objects.all()
    ctx = {"eqiupments":equipment}
    return render(request,'equipment.html',ctx)
      
    

def service_request(request,pk):
    hr=Human_Resource.objects.filter(pk=pk)[0]
    form = ServiceRequestForm()
    if request.method=='POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            fd = form.save(commit = False)
            fd.hr=hr
            fd.for_user = request.user
            fd.save()
            messages.success(request,"Service request has been sent") 
            return redirect('home')
    context = {'form':form}
    return render(request,'hr/request_form.html', context)



@login_required
def user_profileview(request):
    users = Profile.objects.filter(user__pk=request.user.pk)
    if len(users)==1:
        context= {'userprofile':users}
    else:
        context = {'userprofile': None}
    return render(request, 'user_profile.html',context)

def edit_profileview(request, pk):
    try:
        udata = Profile.objects.filter(pk=pk)
        if len(udata)==1:
            form = ProfileForm(instance=udata[0])
        else:
            form = ProfileForm()
        if request.method=='POST':
            if len(udata)==1:
                form = ProfileForm(request.POST, request.FILES, instance=udata[0])
            else:
                form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                fd=form.save(commit=False)
                fd.user=request.user
                fd.email=request.user.email
                fd.save()
                return redirect('up')
        
        context = {"pform":form}
        return render(request, 'edit_profile.html', context)
    except Exception as e:
        print('some error occurred',e)
        return redirect('up')


def contact(request):
    error=""
    if request.method=='POST':
        n = request.POST['cname']
        pn = request.POST['cphone']
        e = request.POST['cemail']
        p = request.POST['cpurpose']
        try:
            Contact.objects.create(con_name=n,con_mobile=pn,con_email=e,con_purpose=p)
            messages.success(request,"Feedback has been save") 
            error = "no"
            return render(request,'contact.html',d)    
        except:
            error="yes"
    d = {'error':error}
    
    return render(request,'contact.html',d)    