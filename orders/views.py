from django.shortcuts import render,get_object_or_404,redirect
from .models import OrderItem,Order
from .forms import OrderCreateForm,OrderUpdateForm,ConfirmationForm
from cart.cart import Cart
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib import messages
from mpesa_api.models import MpesaPayment


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',{'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"order_{}.pdf"'.format(order.id)
    return response


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,'admin/orders/order/detail.html',{'order': order})

@login_required(login_url='/register/')
def order_create(request):
    cart = Cart(request)
    kitu = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.orderer = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
                # clear the cart
            cart.clear()
            return render(request,'orders/order/created.html',{'order': order,'kitu':kitu,'cart':cart})
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart': cart, 'form': form})

@login_required(login_url='/register/')
def order_update(request,order_id):
    order = get_object_or_404(Order, id= order_id) 
    if request.method == 'POST':
        form = OrderUpdateForm(request.POST,request.FILES,instance=order)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Profile has been updated!')
            return redirect('home:order_view')
    else:
        form = OrderUpdateForm(instance=order)
    template = loader.get_template('orders/order_update.html')
    context = {'form':form}
    return HttpResponse(template.render(context,request))


@login_required(login_url='/register/')
def payment_confirmation(request,order_id):
    receipts = MpesaPayment.objects.filter(used=False)
    order = get_object_or_404(Order, id= order_id)
    info = ''
    if request.method == "POST":
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            tcode = form.cleaned_data.get('transaction_code')
            try:
                aaa = MpesaPayment.objects.get(receipt_no = tcode)
            except MpesaPayment.DoesNotExist:
                aaa = None
            if aaa == None:
                info = 'Please enter a valid Mpesa Transaction code.'
            else:
                pesa = aaa.amount
                p = order.get_total_cost()
                if pesa == p and aaa.used == False:
                    order.paid = True
                    aaa.used = True
                    order.save()
                    aaa.save()
                    info = 'Thank you. Your order payment has been confirmed'
                else:
                    info = 'The amount transacted in the transaction code you provided, does not match the amount due for your order,or this code has already been used.Please confirm you entered the correct code.'
    else:
        form = ConfirmationForm()
    form = ConfirmationForm()
    template = loader.get_template('orders/confirmation.html')
    context = {'form': form,'info':info}
    return HttpResponse(template.render(context,request))

@login_required(login_url='/register/')
def delete_order(request,order_id):
    order = get_object_or_404(Order, id= order_id)
    order.delete()
    return redirect('home:order_view')

@staff_member_required
def order_processing(request):
    # packaging
    order = Order.objects.filter(paid=True, delivered= False, packaged= False)
    context = {'order':order, }
    template = loader.get_template('orders/process.html')
    return HttpResponse(template.render(context,request))

@staff_member_required
def packaging(request,order_id):
    order = get_object_or_404(Order, id= order_id)
    order.packaged = True
    order.save()
    return redirect('orders:order_processing')

@staff_member_required
def order_delivery(request):
    order = Order.objects.filter(paid=True, packaged=True, delivered= False)
    context = {'order':order,}
    template = loader.get_template('orders/delivery.html')
    return HttpResponse(template.render(context,request))

@staff_member_required
def make_delivery(request, order_id):
    order = get_object_or_404(Order, id= order_id)
    order.delivered = True
    order.save()
    return redirect('orders:order_delivery')