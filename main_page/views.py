from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, inbound_order, outbound_order
from .forms import ProductForm,InboundForm,OutboundForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q 

# Create your views here.

@login_required
def index(request):
    inbound = inbound_order.objects.all()
    outbound = outbound_order.objects.all()
    products = Product.objects.all()
    context ={
        "inbound": inbound,
        "outbound": outbound,
        "products": products,
    }
    return render(request,"main_page_templates/index.html",context)

def staff_inbound(request):
    inbound = inbound_order.objects.all()
    context ={
        "inbound": inbound,
    }
    return render(request,"main_page_templates/staff_inbound.html",context)

def staff_outbound(request):
    outbound = outbound_order.objects.all()
    context ={
        "outbound": outbound,
    }
    return render(request,"main_page_templates/staff_outbound.html",context)

def staff_inventory(request):
    products = Product.objects.all()
    context ={
        "products": products,
    }
    return render(request,"main_page_templates/staff_inventory.html",context)

def index_inbound(request):
    if request.method == "POST":
        form = InboundForm(request.POST)
        if form.is_valid():
            if Product.objects.filter(sku=form["sku"].value()).exists():
                temp = Product.objects.get(sku=form["sku"].value())
                temp.quantity += int(form["quantity"].value())
                temp.save()
                form.save()
                return redirect("main_page-index")
            else:
                form.save()
                return redirect("main_page-product")      
    else:
        form =InboundForm()
    context = {
        "form": form
    }
    return render(request,"main_page_templates/index_inbound.html",context)

def index_outbound(request):
    if request.method == "POST":
        form = OutboundForm(request.POST)
        if form.is_valid():
            if Product.objects.filter(sku=form["sku"].value()).exists():
                temp = Product.objects.get(sku=form["sku"].value())
                compare = temp.quantity
                if compare > int(form["quantity"].value()):
                    temp.quantity -= int(form["quantity"].value())
                    form.save()
                    return redirect("main_page-index")
                else:
                    messages.error(request, "Quantity exceeds Amount in Quantity.")
            else:
                form.save()
                return redirect("main_page-product")      
    else:
        form =InboundForm()
    context = {
        "form": form
    }
    return render(request,"main_page_templates/index_outbound.html",context)

def index_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page-index")
    else:
        form = ProductForm()
    context = {
        "form": form
    }
    return render(request,"main_page_templates/index_product.html",context)
    

@login_required
def staff(request):
    employee = User.objects.all()
    employee_count = employee.count()
    inbounds_count = inbound_order.objects.all().count()
    outbounds_count = outbound_order.objects.all().count()
    items_count= Product.objects.all().count()
    context ={
        "employee": employee,
        "employee_count": employee_count,
        "inbounds_count": inbounds_count,
        "outbounds_count": outbounds_count,
        "items_count": items_count,
    }
    return render(request,"main_page_templates/staff.html",context)

@login_required
def staff_detail(request, pk):
    employees = User.objects.get(id=pk)
    context ={
        "employees": employees
    }
    return render(request,"main_page_templates/staff_detail.html",context)
    
    
@login_required
def inventory(request):
    items= Product.objects.all()
    employee_count = User.objects.all().count()
    inbounds_count = inbound_order.objects.all().count()
    outbounds_count = outbound_order.objects.all().count()
    items_count = items.count()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main_page-inventory")
    else:
        form = ProductForm()
    context = {
        "items": items,
        "form" : form,
        "employee_count":employee_count,
        "items_count": items_count,
        "inbounds_count": inbounds_count,
        "outbounds_count": outbounds_count,
    }
    return render(request,"main_page_templates/inventory.html", context)

@login_required
def product_delete(request, pk): # primary key of item in question
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("main_page-inventory")
    return render(request,"main_page_templates/product_delete.html")

@login_required
def product_update(request, pk): # primary key of item in question
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect("main_page-inventory")
    else:
        form = ProductForm(instance=item)
    context ={
        "form" : form
    }
    return render(request,"main_page_templates/product_update.html",context)

@login_required
def order(request):
    inbounds = inbound_order.objects.all()
    outbounds = outbound_order.objects.all()
    employee_count = User.objects.all().count()
    items_count= Product.objects.all().count()
    inbounds_count = inbounds.count()
    outbounds_count = outbounds.count()
    context ={
        "inbounds": inbounds,
        "outbounds": outbounds,
        "employee_count": employee_count,
        "items_count": items_count,
        "inbounds_count": inbounds_count,
        "outbounds_count": outbounds_count,
    }
    return render(request,"main_page_templates/order.html",context)

def search(request):
    if request.method == "POST":
        searched =request.POST.get("search")
        if searched != "":
            search_products = Q(Q(name__icontains=searched) | Q(category__icontains=searched) | Q(sku__icontains=searched) | Q(supplier__icontains=searched))
            data = Product.objects.filter(search_products)
            total = data.count()
            context = {
                "searched": searched,
                "data": data,
                "total":total
            }
            return render(request,"main_page_templates/search_result.html",context)
        else:
            result = "Please input your search"+str(searched)
            context ={
                "result":result,
            }
            return render(request,"main_page_templates/search_result.html",context)
    else:
        return render(request,"main_page_templates/search_result.html")
