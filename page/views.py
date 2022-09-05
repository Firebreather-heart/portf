from django.shortcuts import render
import smtplib
import ssl


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
