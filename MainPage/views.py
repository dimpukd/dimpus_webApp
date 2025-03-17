from django.http import HttpResponse
from django.shortcuts import render
from .models import food,wine,other_products
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def home(request):
    food1 = food.objects.all()
    wine1 = wine.objects.all()
    other_products1 = other_products.objects.all()
    return render(request, 'index.html', {'foods':food1, 'wines':wine1, 'other_products':other_products1})

def aboutus(request):
    return render(request, 'about.html')

def contactus(request):
    return render(request, 'contact.html')

from django.shortcuts import redirect
from urllib.parse import urlencode

# def contact_submit(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")

#         # Format WhatsApp message
#         whatsapp_message = f"New Contact Form Submission:\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        
#         # Encode the message for URL compatibility
#         encoded_message = urlencode({"text": whatsapp_message})

#         # Your WhatsApp number (with country code, but without +)
#         whatsapp_number = "+919482864273"  # Change this to your number

#         # Redirect to WhatsApp chat with pre-filled message
#         return redirect(f"https://api.whatsapp.com/send?phone={whatsapp_number}&{encoded_message}")

#     return HttpResponse("Invalid Request", status=400)


def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Email content
        subject = "New Contact Form Submission"
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        from_email = "dimpu8289@gmail.com"  # Must match EMAIL_HOST_USER in settings.py
        to_email = ["machamma1940@gmail.com"]  # Your email (recipient)

        # Send email automatically
        send_mail(subject, body, from_email, to_email, fail_silently=False)

       # return HttpResponse("Message sent via email successfully!")

        messages.info(request, 'Thank you for your  message, we will get back to you very Soon!!')
        return redirect('contact_us')

    return HttpResponse("Invalid Request", status=400)



def submit_order(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        product_name = request.POST.get("product_name")
        quantity = request.POST.get("quantity")
        date = request.POST.get("date")
        address = request.POST.get("address")

        # Email content
        subject = "New Order"
        body = f"Name: {name}\nPhone: {phone}\nProduct Name : {product_name}\nQuantity : {quantity}\n Date: {date}\nAddress: {address}"
        from_email = "dimpu8289@gmail.com"  # Must match EMAIL_HOST_USER in settings.py
        to_email = ["machamma1940@gmail.com"]  # Your email (recipient)

        # Send email automatically
        send_mail(subject, body, from_email, to_email, fail_silently=False)

       # return HttpResponse("Message sent via email successfully!")

       # messages.info(request, 'Thank you for your Order, we will get back to you very Soon!!')
        return redirect('/?order_success=1')

    return HttpResponse("Invalid Request", status=400)



