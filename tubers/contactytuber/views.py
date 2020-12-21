from django.shortcuts import redirect, render
from django.contrib import messages
from .models import ContactYtuberTeam
# Create your views here.


def contactytuberteam(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        email = request.POST['email']
        company_name = request.POST['company_name']
        subject = request.POST['subject']
        message = request.POST['message']

        # VALIDATIONS CAN BE DONE

        contact_obj = ContactYtuberTeam(
            full_name=full_name, phone=phone, email=email, company_name=company_name,
            subject=subject, message=message)

        contact_obj.save()
        messages.success(request, 'Thank you for contacting us!')
        return redirect('home')
