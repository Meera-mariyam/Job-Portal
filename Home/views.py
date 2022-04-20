import email
from urllib import request
from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.conf  import settings
from django.urls import reverse_lazy
from Home.models import Login,Company,Candidate
from django.views.generic import UpdateView
from django.views.generic import View,TemplateView
from django.contrib import messages
from django.contrib import auth

# Create your views here.
class Index(TemplateView) :
    template_name = 'Home/index.html'

class About(TemplateView):
    template_name = 'Home/about.html'
    

class  Contact(TemplateView):
    '''return render(request,'Home/contact.html')'''
    template_name = 'Home/contact.html'

class  Candreg(View):
    def get(self,request):
        return render(request,'Home/candidate_reg.html')
    def post(self,request):
        #logincn = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        cal =Login(email= email,password =password,category = 'candidate',status = 0)
        cal.save()
        name = request.POST.get('name')
        addr = request.POST.get('address')
        dob = request.POST.get('dob')
        phone = request.POST.get('phonenumber')
        state = request.POST.get('state')
        place = request.POST.get('place')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        username =request.POST.get('username')
        Candidate(candidatename = name,address = addr,dob = dob,phone = phone,state = state,place = place,qualification = qualification,gender = gender,email = email,login=cal,username = username,status = 0).save()
        messages.info(request,'Thank you for registration..wait for admin approval..')
        return redirect('home_index')
        #return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/home_index';</script>")

class Companyreg(View):
    def get(self,request):
        return render(request,'Home/company_reg.html')

    def post(self,request):
        #logincm = Login()
        email = request.POST.get('email')
        password = request.POST.get('password')
        lc = Login(email= email,password =password,category = 'company',status = 0)
        lc.save()

    
        #comp = Company()
        companyname = request.POST.get('companyname')
        regid = request.POST.get('cregid')
        address = request.POST.get('address')
        phone = request.POST.get('phonenumber')
        state = request.POST.get('state')
        place = request.POST.get('place')
        owner = request.POST.get('owner')
        websiteid = request.POST.get('websiteid')
        desp = request.POST.get('description')
        email = request.POST.get('email')
        username = request.POST.get('username')
       # comp.login = logincm
       # comp.save()
        Company(companyname =companyname,regid = regid,address = address,phone = phone,state = state,place = place,companyowner = owner,websiteid = websiteid,description = desp,email = email,login=lc,username = username,status = 0).save()
        messages.info(request,'Thank you for registration..wait for admin approval..')
        return redirect('home_index')
        #return HttpResponse("<script>alert('Thank you for registration..wait for admin approval..');window.location ='/home_index';</script>")

class LoginView(View):
    def get(self,request):
        return render(request,"Home/login.html")
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if (Login.objects.filter(email=email, password=password).exists()):
            logins = Login.objects.filter(email=email, password=password)
            for login in logins:

                #login=Login()
                usertype = login.category
                status = login.status
                request.session["usertype"] = usertype
                request.session["status"] = status
                if ((usertype == "admin")&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'adminhome/adminhome.html')
                elif ((usertype == 'candidate')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'candidate/candidate.html')
                elif ((usertype == 'company')&(status == 1 )):
                    request.session["email"] = login.email
                    request.session["password"] = login.password
                    request.session["usertype"] = login.category
                    request.session["status"] = login.status
                    request.session["userid"] = login.pk
                    return render(request,'company/company.html')

                else:
                    template = loader.get_template("home/login.html")
                    context = {"error": "Incorrect username or password"}
                    return HttpResponse(template.render(context, request))

                    # dic = {'msg': 'Invalid user name or password'}
                    # return render(request, 'login.html', context=dic)
        else:
            template = loader.get_template("home/login.html")
            context = {"error": "Incorrect Information"}
            return render(request,'candidate/candidate.html')

'''
class LoginView(View):
    def get(self,request):
        return render(request,"Home/login.html")
    def post(self,request):
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(username=email,password=password)
        #print(user)
        if email == 'admin@gmail.com':
            request.session["email"] = email
            return redirect('Adminhomee')
        if user is not None:
            request.session["email"] = email
            auth.login(request,user)
            #send_mail('Login successful','Welcome to our mini bookstore!!',settings.EMAIL_HOST_USER,[username])
            #request.session['AUTHSESSION']=username
            return redirect('Candidatehome')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')


'''

class Candidatehome(TemplateView):
    template_name = 'candidate/candidate.html'
    