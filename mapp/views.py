from django.shortcuts import render
from django.http import HttpResponse
from mapp.models import CustomUser
import smtplib,time
from django.contrib.auth.hashers import make_password
from django.urls import reverse
import base64   
def index(request):

    return render(request, "reset_password.html")   
    
def sendverfication(s):
    return render(s ,"sendverfication.html")
class reset_password:
    def send(reques):
        email=reques.POST['email']    
        try:
            check= CustomUser.objects.get(email=email)
            smtp_ssl = None
            smtp_ssl = smtplib.SMTP_SSL(host="smtp.gmail.com", port=465)
            resp_code, response = smtp_ssl.login(user="symbitimetable@gmail.com", password="olvuvmzjbcqyetei")
            current_time=str(time.time()+30)
            encoded_email= current_time+"_"+email
            encoded_email= base64.b64encode(encoded_email.encode()).decode()
            reverseurl = reverse("mapp:updated",args=[encoded_email])
            response = smtp_ssl.sendmail(from_addr='symbitimetable@gmail.com',
                             to_addrs=[email],
                            msg='Subject: {}\n\n{}'.format("sample subject", "this is a sample message"+ "\n http://127.0.0.1:8000/"+reverseurl)
                           )    
            
            return HttpResponse()
        except Exception as e:
            return HttpResponse("reverseurl")     
    def updated(request, arg1):
        
        if request.method =="POST":
            decoded_email = base64.b64decode(arg1).decode()
            email = decoded_email.split("_")
            if float(email[0]) > float(time.time()):
                check= CustomUser.objects.get(email=email[1])
                h_password=request.POST['update']
                h_password = make_password(h_password)
                check.password=h_password
                check.save()        
                return HttpResponse(arg1)
            else:
                return HttpResponse("expired")    
            
        else:
            return render(request, "updatepassword.html")
        
        
