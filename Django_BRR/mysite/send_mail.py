from dotenv import dotenv_values
from django.core.mail import send_mail

config = dotenv_values("Django_BRR\OpenBRR\credentials.env")

def send(config):
    send_mail(
        'Asunto', # Asunto
        'Mensaje', # Cuerpo del mensaje
        'i.miguel.molinero@gmail.com', # Usuario que envía el email
        ['i.miguel.molinero@gmail.com'], # Usuario al que se envía el email
        fail_silently=False,
    )

send(config)