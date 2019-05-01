from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404

from coingate_api import CoingateAPI, api_error
from datetime import datetime, timezone
import secrets

from payment.models import Order
from payment.forms import PriceForm

sand_auth_token = '3CAtNg3ZUFdbVJKN6DFk2gy5eHVS1T8sP_Hybtbe'
product_categorical_prices = [100, 200, 300, 400, 500] # just populate with dummy data right now
products_categorical = ['PRODUCT1', 'PRODUCT2', 'PRODUCT3', 'PRODUCT4', 'PRODUCT5']

def order_status(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        form = PriceForm()

        context ={
            'orders': orders,
            'form': form
        }

        return render(request, 'order_status.html', context)
    elif request.method == 'POST':
        form = PriceForm(request.POST)
        # check if form is valid
        if form.is_valid():
            products = form.cleaned_data['products']
            price = int(form.cleaned_data['price'])
            # calculate payment price (product_categorical_prices[products[0]] * price)
            payment_price = product_categorical_prices[int(products[0])] * price

            context = {
                'products': products_categorical[int(products)],
                'payment_price': payment_price
            }
            #request.session['payment_price'] = payment_price

            return render(request, 'payment_proceed.html', context=context)



def payment_proceed(request, payment_price):
    
    if request.method == 'POST':
        try:
            api = CoingateAPI(auth_token=sand_auth_token, environment='sandbox')
            order_id = 'coingate_' + str(datetime.now(tz=timezone.utc))
            token = secrets.token_hex()
        
            result = api.create_order(
                price_amount=payment_price,
                price_currency='USD',
                receive_currency="do not convert",
                order_id=order_id,
                title="New payment for {}".format(payment_price),
                description="paying for {}".format(payment_price),
                token=token,
                callback_url="http://localhost:8000/callback",
                cancel_url="http://localhost:8000/cancel",
                success_url="http://localhost:8000/success"
            )

            order_instance = Order(order_id=result['id'], order_status=True)
            order_instance.save()

            return HttpResponseRedirect(result['payment_url'])
        except api_error.APIError as e:
            raise Http404 (e)

def callback(request):
    return render(request, 'callback.html')

def cancel(request):
    try:
        api = CoingateAPI(auth_token=sand_auth_token, environment='sandbox')

        orders = Order.objects.all()
        order_id = orders.values('order_id').last()['order_id']
        result = api.checkout(order_id)

        if result['status'] == 'invalid':
            order_instance = Order.objects.get(order_id=result['id'])
            order_instance.order_status = False
            order_instance.save()
        
        context = {
            'result': result
        }
        return render(request, 'cancel.html', context=context)
    except api_error.APIError as e:
        raise Http404 (e)
    

def success(request):
    try:
        api = CoingateAPI(auth_token=sand_auth_token, environment='sandbox')

        orders = Order.objects.all()
        order_id = orders.values('order_id').last()['order_id']
        result = api.checkout(order_id)

        if result['status'] == 'paid':
            context = {
                "status": True,
                "api_result": result
            }
        else:
            context = {
                "status": False,
                "api_result": result
            }
    
        return render(request, 'success.html', context=context)
    except api_error.APIError as e:
        raise Http404 (e)
