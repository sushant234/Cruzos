from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from app.models import *
import random
from django.db import connection
from collections import namedtuple
import razorpay
import http.client
import smtplib
from cart.cart import Cart

# Create your views here.


def index(request):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    context = {}
    context['mpc'] = meatproductcategories.objects.all()
    return render(request,'index.html',context)

def products(request,value):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    context={}
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_product WHERE fid_id = %s',[value])
        results = namedtuplefetchall(cursor)  
        print(results)
    context['product'] = results
    return render(request,'products.html', context)

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def services(request):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    context={}
    context['service'] = service.objects.all()
    return render(request,'services.html', context)

def orderform(request,value):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    context={}
    print(value)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_cartt WHERE sessionid = %s',[value])
        results = namedtuplefetchall(cursor) 
    print(results)
    a = 0
    a1=""
    for i in results:
        b = i.price * i.quantity
        head = i.heading
        print(head)
        a +=b
        c = head + " price: " + str(i.price) + ", quantity: " + str(i.quantity)
        a1 +=c
        print(a1)
    context['a'] = a
    if "butt3" in request.POST:
        name = request.POST['name']
        request.session['name'] = name
        print(name)
        phone = request.POST['phone']
        request.session['phone'] = phone
        print(phone)
        email = request.POST['email']
        request.session['email'] = email
        print(email)
        address = request.POST['message']
        print(address)
        town = request.POST['town']
        print(town)
        codd = request.POST.get('cod',0)
        print(codd)
        # quantity = request.POST['quantity']
        # print(quantity)
        if (codd == "on"):
            cod = customerorderdetails(name=name, phone=phone, email=email, address=address, town=town, totalamount=int(a), city='Mumbai',  sid=value)
            cod.save()
            s = smtplib.SMTP('smtp.gmail.com', 587)  
            s.starttls() 
            s.login("example@gmail.com", "password") 
            message = "Subject: Order Received\n" +  "Cash on delivery" + "Your order is placed successfully.\n" +" Hi " +  name +"!\n" + "\nOrder Details " + a1 +"\nYour order is getting prepared, it will be delivered within next day between 11am to 8pm. Thanks for your patience."
            s.sendmail("example@gmail.com", email,message)  
            s.quit()
            print('**')
            s1 = smtplib.SMTP('smtp.gmail.com', 587)  
            s1.starttls() 
            s1.login("example@gmail.com", "Cruz@123") 
            message = "Subject: Order Received for Cash on Delivery\n" + "Your order is placed successfully.\n" +"Name of the Customer: " +  name +"!\n" + "\nOrder Details: "+ a1 + "\nMail ID: " + email + "\nPhone No.: " + str(phone) + "\nAddress: " + address + "\nYour order is getting prepared, it will be delivered within next day between 11am to 8pm. Thanks for your patience."
            s1.sendmail("example@gmail.com", "example1@gmail.com", message)  
            s1.quit()
            with connection.cursor() as cursor:
                cursor.execute('SELECT * FROM app_cartt WHERE sessionid = %s',[sid])
                results = namedtuplefetchall(cursor)  
                print(results[0].quantity)
            for i in results:
                b = i.heading
                c = i.quantity
                n = product.objects.filter(heading=b).values_list('stock', flat=True)
                print(n)
                m = dict(Mobile=list(n))
                print(m)
                m1 = m['Mobile']
                print(m1)
                cc = str(m1)[1:-1]
                print(cc)
                cc1 = int(cc)
                upstock = cc1 - c
                if upstock == 0:
                    s = smtplib.SMTP('smtp.gmail.com', 587)  
                    s.starttls() 
                    s.login("example@gmail.com", "password") 
                    message = "Subject: Product is out of stock\n" + "Product " + b + " is out of stock, kindly update your stock."
                    s.sendmail("gmail@gmail.com", "example1@gmail.com",message)  
                    s.quit()
                product.objects.filter(heading=b).update(stock=upstock)
            del request.session['sid']
            print('*3')
            del request.session['cart']
            print('*4')
            context = {}
            print('*5')
            context['mpc'] = meatproductcategories.objects.all()
            print('*6')
            return render(request,'index.html',context)
        else:
            cod = customerorderdetails(name=name, phone=phone, email=email, address=address, town=town, totalamount=int(a), city='Mumbai',  sid=value)
            cod.save()
            prc2 = a * 100
            # print('********')
            # with connection.cursor() as cursor:
            #     cursor.execute('SELECT * FROM app_product WHERE fid_id = %s',[value])
            #     results = namedtuplefetchall(cursor)  
            # print(results[0].price)
            # prc = int(results[0].price)
            # prc1  = prc*100
            # prc2 = prc1*int(quantity)
            # print(prc)
            # print(prc1)
            # print(prc2)
            n1 = random.randint(00000,99999)
            print(n1)
            client = razorpay.Client(auth=("rzp_test_di7k5vD6oRZtV5jvkjvnf", "TSUr0nWhhJOrsbw6YZ73XWD9jhvjhvhvh"))
            client.set_app_details({"title" : "Django", "version" : "3.7.3"})
            order_currency = 'INR'
            order_receipt = 'order_rcptid_' + str(n1)
            print(order_receipt)
            notes = {
                'shipping address': address + ' ' + town + ' ' + 'Mumbai'
            }
            print(notes['shipping address'])
            response = client.order.create(dict(amount=prc2, currency=order_currency,receipt=order_receipt,notes=notes,payment_capture='0'))
            order_id = response['id']
            request.session['orderid'] = order_id
            order_status = response['status']
            if order_status=='created':
                context['product_id'] = value
                context['price'] = prc2
                context['name'] = name
                context['phone'] = phone
                context['email'] = email
                context['order_id'] = order_id
                return render(request, 'extendorderform.html', context)
    return render(request,'orderform.html',context)

def privacypolicy(request):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    return render(request,'privacypolicy.html')

def tc(request):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    return render(request,'T&C.html')

def extends(request):
    return render(request,'extendorderform.html')

def payment_status(request):
    sid = request.session['sid']
    response = request.POST
    orderid1 = request.session['orderid']
    print(orderid1)
    cart = Cart(request)
    cart.clear()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_cartt WHERE sessionid = %s',[sid])
        results = namedtuplefetchall(cursor) 
    print(results)
    a = 0
    a1=""
    for i in results:
        b = i.price * i.quantity
        head = i.heading
        print(head)
        a +=b
        c = head + " price: " + str(i.price) + ", quantity: " + str(i.quantity)
        a1 +=c
        print(a1)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_customerorderdetails WHERE sid = %s',[sid])
        results = namedtuplefetchall(cursor)  
    print(results)
    print(results[0].email)
    print(results[0].name)
    print(results[0].phone)
    email = results[0].email
    print(email)
    name = results[0].name
    phone = results[0].phone
    address = results[0].address
    town = results[0].town
    print(response)
    params_dict = {
        'razorpay_payment_id':response['razorpay_payment_id'],
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_signature':response['razorpay_signature']
    }
    # try:
    client = razorpay.Client(auth=("rzp_test_di7k5vD6oRZtV5ghvhvhjvhj", "TSUr0nWhhJOrsbw6YZ73XWD9hhjvjhvhvhv"))
    client.set_app_details({"title" : "Django", "version" : "3.7.3"})
    status = client.utility.verify_payment_signature(params_dict)
    print(status)
    s = smtplib.SMTP('smtp.gmail.com', 587)  
    s.starttls() 
    s.login("example@gmail.com", "password") 
    # message = "Subject: Order Received\n" + "Your order is placed successfully.\n" +" Hi " +  name +"!\n" + "Order ID: " + orderid1 + "\nYour order is getting prepared, it will be delivered within 2 hours. Thanks for your patience."
    message = "Subject: Order Received\n" + "Online Payment received!" + "Your order is placed successfully.\n" +" Hi " +  name +"!\n" + "\nOrder Details " + a1 +"\nYour order is getting prepared, it will be delivered next day between 11am to 8pm. Thanks for your patience."
    s.sendmail("example@gmail.com", email,message)  
    s.quit()
    print('**')
    s1 = smtplib.SMTP('smtp.gmail.com', 587)  
    s1.starttls() 
    s1.login("example@gmail.com", "Cruz@123") 
    # message = "Subject: Order Received\n" + "Your order is placed successfully.\n" +"Name of the Customer: " +  name +"!\n" + "Order ID: " + orderid1 + "\nMail ID: " + email + "\nPhone No.: " + str(phone) + "\nYour order is getting prepared, it will be delivered within 2 hours. Thanks for your patience."
    message = "Subject: Order Received by online payment\n" + "Your order is placed successfully.\n" +"Name of the Customer: " +  name +"!\n" + "\nOrder Details "+ a1 + "\nMail ID: " + email + "\nPhone No.: " + str(phone) + "\nAddress: " + address + " " + town + "\nYour order is getting prepared, it will be delivered next day between 11am to 8pm. Thanks for your patience."
    s1.sendmail("example@gmail.com", "example1@gmail.com", message)  
    s1.quit()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_cartt WHERE sessionid = %s',[sid])
        results = namedtuplefetchall(cursor)  
    print(results[0].quantity)
    for i in results:
        b = i.heading
        c = i.quantity
        n = product.objects.filter(heading=b).values_list('stock', flat=True)
        print(n)
        m = dict(Mobile=list(n))
        print(m)
        m1 = m['Mobile']
        print(m1)
        cc = str(m1)[1:-1]
        print(cc)
        cc1 = int(cc)
        upstock = cc1 - c
        if upstock == 0:
            s = smtplib.SMTP('smtp.gmail.com', 587)  
            s.starttls() 
            s.login("example@gmail.com", "password") 
            message = "Subject: Product is out of stock\n" + "Product " + b + " is out of stock, kindly update your stock."
            s.sendmail("example@gmail.com", "example1@gmail.com",message)  
            s.quit()
        product.objects.filter(heading=b).update(stock=upstock)
    print('*1')
    del request.session['orderid']
    print('*2')
    del request.session['sid']
    print('*3')
    del request.session['cart']
    print('*4')
    context = {}
    print('*5')
    context['mpc'] = meatproductcategories.objects.all()
    print('*6')
    return render(request,'index.html',context)
    # except:
    #     s = smtplib.SMTP('smtp.gmail.com', 587)  
    #     s.starttls() 
    #     s.login("help.zapped@gmail.com", "zapped#1234") 
    #     message = "Subject: Order Failed\n" + "hello! your order is not confirmed due to payment failure." 
    #     s.sendmail("help.zapped@gmail.com", email, message)  
    #     s.quit()
    #     s = smtplib.SMTP('smtp.gmail.com', 587)  
    #     s.starttls() 
    #     s.login("help.zapped@gmail.com", "zapped#1234") 
    #     message = "Subject: Order Failed\n" +"Your order is failed!.\n" +"Name of the Customer: " +  name +"!\n" + "Order ID: " + str(orderid1) + "\nMail ID: " + email + "\nPhone No.: " + str(phone) + "\nYour order is getting prepared, it will be delivered within 2 hours. Thanks for your patience."
    #     s.sendmail("help.zapped@gmail.com", "rahuliyer1996@gmail.com", message)  
    #     s.quit()
    #     del request.session['orderid']
    #     del request.session['sid']
    #     del request.session['cart']
    #     context = {}
    #     context['mpc'] = meatproductcategories.objects.all()
    #     return render(request,'index.html',context)


def cart_add(request, id):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    cart = Cart(request)
    print(id)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_product WHERE id = %s',[id])
        results = namedtuplefetchall(cursor)  
    print(results[0].price)
    prc = results[0].price
    print(results[0].quantity)
    qty = results[0].quantity
    print(results[0].heading)
    hdg = results[0].heading
    if cartt.objects.filter(heading=hdg, sessionid=sid).exists():
        n = cartt.objects.filter(heading=hdg, sessionid=sid).values_list('quantity', flat=True)
        m = dict(Mobile=list(n))
        m1 = m['Mobile']
        c = str(m1)[1:-1]
        print(c)
        qty2 = int(c)
        qty1 = int(qty2) + 1
        cartt.objects.filter(heading=hdg, sessionid=sid).update(quantity=qty1)
    else:
        crt = cartt(price=prc, quantity=qty, heading=hdg, sessionid= sid)
        crt.save()
    product1 = product.objects.get(id=id)
    cart.add(product=product1)
    a = request.session['cart']
    b = request.session.get('cart')
    print(b)
    # print(a)
    for i in a:
        # print(a[i])
        for j in a[i]:
            print(a[i][j])
            # if a[i][j] == '3':
            #     print(a[i][j])
            #     print('**')
    return redirect("cart_detail")

def cart_detail(request):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    context={}
    if cartt.objects.filter(sessionid=sid).exists():
        a = 1
        context['a'] = a
        context['sid'] = sid
    else:
        a = 0
        context['a'] = a
    return render(request, 'cart.html',context)

def item_increment(request, id):
    print(id)
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    cart = Cart(request)
    product1 = product.objects.get(id=id)
    cart.add(product=product1)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_product WHERE id = %s',[id])
        results = namedtuplefetchall(cursor)  
    print(results[0].heading)
    hdg = results[0].heading
    print(results[0].quantity)
    # qty = results[0].quantity
    # print(qty)
    if cartt.objects.filter(heading=hdg, sessionid=sid).exists():
        n = cartt.objects.filter(heading=hdg, sessionid=sid).values_list('quantity', flat=True)
        m = dict(Mobile=list(n))
        m1 = m['Mobile']
        c = str(m1)[1:-1]
        print(c)
        qty = int(c)
        qty1 = int(qty) + 1
        print(qty1)
        cartt.objects.filter(heading=hdg, sessionid=sid).update(quantity=qty1)
        print('item increment')
    return redirect("cart_detail")
    # return HttpResponseRedirect("cart_detail#services1-1l")
    # return render(request,'cart.html')


def item_decrement(request, id):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    print('*')
    sid = request.session['sid']
    print('*1')
    cart = Cart(request)
    print('*2')
    product1 = product.objects.get(id=id)
    print('*3')
    # cart.decrement(product=product1)
    # print('**')
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_product WHERE id = %s',[id])
        results = namedtuplefetchall(cursor)
        print('***')
    print(results[0].heading)
    hdg = results[0].heading
    print('****')
    if cartt.objects.filter(heading=hdg, sessionid=sid).exists():
        n = cartt.objects.filter(heading=hdg, sessionid=sid).values_list('quantity', flat=True)
        m = dict(Mobile=list(n))
        m1 = m['Mobile']
        c = str(m1)[1:-1]
        print(c)
        qty = int(c)
        if qty > 1:
            qty1 = int(qty) - 1
            print(qty1)
            cartt.objects.filter(heading=hdg, sessionid=sid).update(quantity=qty1)
            cart.decrement(product=product1)
            print('**')
            print('item decrement')
        else:
            print('*5')
            pass
    return redirect("cart_detail")

def item_clear(request, id):
    if 'sid' not in request.session:
        n = random.randint(1000000000,9999999999)
        request.session['sid'] = n
        print(request.session['sid'])
    else:
        print(request.session['sid'])
        pass
    sid = request.session['sid']
    cart = Cart(request)
    product1 = product.objects.get(id=id)
    cart.remove(product1)
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM app_product WHERE id = %s',[id])
        results = namedtuplefetchall(cursor)
        print('***')
    print(results[0].heading)
    hdg = results[0].heading
    if cartt.objects.filter(heading=hdg, sessionid=sid).exists():
        cartt.objects.filter(heading=hdg, sessionid=sid).delete()
    return redirect("cart_detail")


def contactus(request):
    return render(request,'contactus.html')