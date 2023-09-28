import smtplib
import ssl
from datetime import datetime

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import TemplateView

from home.models import validate_time_slot, Appointment
from .models import time_slots


def send_e_mail(receiver_email, text):
    sender_email = "email"

    password = 'app passwrod'

    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465,
                              context=context)
    server.login(sender_email, password)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)
    server.close()


def send_email_view(request):
    subject = 'Hello, Aswin'
    html_message = render_to_string('mail.html')
    plain_message = strip_tags(html_message)
    from_email = 'your_email@gmail.com'
    recipient_list = ['admin@gmail.com']
    send_mail(subject, plain_message, from_email,
              recipient_list, html_message=html_message)

    return HttpResponse('Email sent successfully')


class IndexView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_slots'] = time_slots
        return context

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            self.get_context_data())

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login?next=/')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        department = request.POST.get('department')

        date_obj = datetime.strptime(date,
                                     '%Y-%m-%d').date()
        status, message = validate_time_slot(time, date_obj)
        print(status, message)
        if status:
            Appointment.objects.create(
                user=request.user,
                name=name,
                email=email,
                phone=phone,
                date=date,
                time=time,
                department=department
            )
            return HttpResponse('Appointment Booked')
        else:

            return self.render_to_response(
                self.get_context_data(error=message))


class ContactView(TemplateView):
    template_name = 'home/contact.html'

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            self.get_context_data())

    def post(self, request, *args, **kwargs):
        print('hi')
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message_subject = request.POST.get(
            'message-subject')
        umessage = request.POST.get('umessage')
        subject = f'New message:{message_subject}'
        message = f'From:{message_name}\nEmail:{message_email}\n\n{umessage}'
        from_email = 'sunithvs2002@gmail.com'
        recipient_list = ['hi@sunithvs.com']

        send_e_mail(recipient_list, message)

        return HttpResponse('Thank you for your message')


def error_404_view(request, exception):
    return render(request, '404.html')


def error_500_view(request):
    return render(request, '500.html')
