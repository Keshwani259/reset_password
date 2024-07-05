from django.urls import path
from . import views
app_name = "mapp"
urlpatterns=[
        path("",views.index, name="mainpage"),
        

        path("sendverfication", views.sendverfication, name ="verfication"),
        
        path("send", views.reset_password.send ,name ="send"),
        path('updated/<arg1>',views.reset_password.updated,name ="updated"),
        ]
