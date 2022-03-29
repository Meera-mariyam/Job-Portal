from urllib import request
from django.shortcuts import redirect, render
from django.http import HttpResponse,HttpResponseRedirect
from django.conf  import settings
from Home.models import Company,Candidate,Login
from Company.models import Vacancies
from Candidate.models import ApplyVacancy
from django.core.checks import messages
from django.contrib import messages
from django.views.generic import View,TemplateView,FormView

class Companyhome(TemplateView):
    template_name = 'company/company.html'
    

class Addvacancy(View):
    def get(self,request):
        return render( request,'Company/addvacancy.html')

    def post(self,request):
        lid = request.session.get('userid')
        cid = Company.objects.get(login_id=lid)
        compid = cid.id
        refcode = request.POST.get("referenceid")
        jobtitle = request.POST.get("jobtitle")
        description = request.POST.get("description")
        skills = request.POST.get("skills")
        qualification = request.POST.get("qualification")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pincode = request.POST.get("pincode")
        experience = request.POST.get("experience")
        opening = request.POST.get("opening")
        publishedon = request.POST.get("publishedon")
        dateapply = request.POST.get("dateapply")
        venue = request.POST.get("venue")
        contact = request.POST.get("contact")
        '''vacan = Vacancies()
        vacan.companyid_id = compid
        vacan.login_id = lid
        vacan.reference_code = refcode
        vacan.jobtitle = jobtitle
        vacan.description = description
        vacan.keyskill = skills
        vacan.qualification = qualification
        vacan.city = city
        vacan.state = state
        vacan.pincode = pincode
        vacan.experience = experience
        vacan.no_opening = opening
        vacan.publishedon = publishedon
        vacan.lastdate = dateapply
        vacan.joblocation = venue
        vacan.contactno = contact
        vacan.status =1
        vacan.save()'''
        Vacancies(companyid_id = compid,login_id = lid,reference_code = refcode,jobtitle = jobtitle,description = description,keyskill = skills,qualification = qualification,city = city,state = state,pincode = pincode,experience = experience,no_opening = opening,publishedon = publishedon,lastdate = dateapply,joblocation = venue,contactno = contact,status =1).save
        messages.info(request,'Successfully added vacancy')
        #return HttpResponse("<script>alert('Successfully add vacancy');window.location ='company/company.html';</script>")
        return render(request,'company/company.html')

    '''
def update_comp(request,id):
    d = Company.objects.all(id=id)
    return render(request,'updatecompany.html',{'edit':d})
    
def updateprocess(request,id):
    d = Company.objects.all(id=id)
    d.companyname=request.POST.get('companyname')
    d.regid=request.POST.get('regid')
    d.addres=request.POST.get('address')
    d.phone=request.POST.get('phonenumber')
    d.state=request.POST.get('state')
    d.place=request.POST.get('place')
    d.companyowner=request.POST.get('companyowner')
    d.websiteid=request.POST.get('websiteid')
    d.description=request.POST.get('description')
    d.email=request.POST.get('email')
    d.username=request.POST.get('username')
    d.save(Companyhome)

    messages.success(request,'Updated Successfully') 
    return redirect()   

    '''
class Application(View):
    def get(self,request):
        lid = request.session.get('userid')
        vacn = Vacancies.objects.all()
        app = ApplyVacancy.objects.all()
        context = {'vacn': vacn, 'lid': lid,'app':app}
        return render(request, 'company/appvacancy.html', context)
'''
class idvacancy(request,id):
    vacn = Vacancies.objects.all()
    context = {'vacn': vacn,'id':id}
    return render(request, 'company/idvacancies.html', context)

'''

def clogout(request):
    try:
      del request.session['email']
    except:
      pass
    messages.info(request,'You are successfully logged off')
    return redirect('login')
    #return HttpResponse("<script>alert('you are successfully Logged off..');window.location ='/login';</script>")

