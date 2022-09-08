from django.shortcuts import render,redirect
import smtplib
import ssl,threading
from .main import sendmail
from django.http import JsonResponse


# Define the transport variables
ctx = ssl.create_default_context()
password = "ibueubjmfcfdxisx"    # Your app password goes here
sender = "lordfirebcorps@gmail.com"    # Your e-mail address
receiver = "dtenny95@gmail.com" # Recipient's address



# Create your views here.
def index(request):
    return render(request,'homepage.html')

def messageme(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub =  request.POST.get('subject')
        msg = request.POST.get('message')

        message = f'''{name} sent you a message, with subject {sub},
                full message: {msg}
                reply to {email}
         '''
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
        except:
            pass 
    return render(request, 'homepage.html')

def register(request, ):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        email = request.POST.get('email')
        number = request.POST.get('phone')

        message =  f"""
            {surname} {firstname}, Date of Birth {age}  just registered with
            email {email} and phone {number}
        """
        try:
            t=threading.Thread(sendmail(message, 'dtenny95@gmail.com','Course Registration',))
            t.start()
        except:
            pass
    return redirect('home')


        
