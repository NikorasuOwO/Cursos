from django.core.mail import send_mail
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
send_mail("Asunto",
        "Mensaje",
         "axiomaticamatesinfo@gmail.com",
         ["axiomaticamatesinfo@gmail.com"],
         fail_silently=False)
