from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Hiretuber

# Create your views here.


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        user_id = request.POST['user_id']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']

        # VALIDATIONS CAN BE DONE
        tubers_hired = Hiretuber.objects.filter(user_id=user_id)
        if tubers_hired.filter(tuber_id=tuber_id).exists():
            messages.warning(
                request, 'Sorry! You have already hired {}'.format(tuber_name))
            return redirect('youtubers')

        else:

            hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, tuber_id=tuber_id, tuber_name=tuber_name,
                                  city=city, phone=phone, state=state, message=message, user_id=user_id)

            hiretuber.save()
            messages.success(request, 'Thank you for reaching out!')
            return redirect('youtubers')
