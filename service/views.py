from doctor.views import appointment
from customer.models import Customer
from vendor.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import transaction
from django.core.paginator import Paginator


from django.shortcuts import redirect, render
from .forms import MicrobiologyForm, ChemistryForm, HematologyForm, BloodBankForm, MolecularDiagnoticsForm, ReproductiveBiologyForm, AppointmentForm, UploadFileForm, LabReportForm
from lab.models import Lab
from .models import Appointment, LabAppointment, Service


@login_required
@transaction.atomic
def createMicrobiology(request):
    form = MicrobiologyForm(request.POST or None)

    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')
        except:
            return redirect('/lab/dashboard/')
    return render(request,'service/microbiology.htm', {'form' : form})

@login_required
@transaction.atomic
def createChemistry(request):
    form = ChemistryForm(request.POST or None)

    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')

        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/chemistry.htm', {'form' : form})

@login_required
@transaction.atomic
def createHematology(request):
    form     = HematologyForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')

        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/hematology.htm', {'form' : form})

@login_required
@transaction.atomic
def createBloodBank(request):
    form = BloodBankForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')

        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/bank.htm', {'form' : form})

@login_required
@transaction.atomic
def createMolecularDiagnotics(request):
    form = MolecularDiagnoticsForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')

        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/diagnotics.htm', {'form' : form}) 

@login_required
@transaction.atomic
def createReproductiveBiology(request):
    form = ReproductiveBiologyForm(request.POST or None)
    if form.is_valid():
        try : 
            service = form.save(commit=False)
            service.lab = Lab.objects.filter(user=request.user).first()
            service.service_type = request.POST.get('service_type')
            service.save()
            return redirect('/lab/dashboard/')

        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/reproductive.htm', {'form' : form})           

@login_required
def listServices(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Service',
                }
        services_list = Service.objects.all()
        paginator = Paginator(services_list, 10)

        page_number = request.GET.get('page')
        services = paginator.get_page(page_number)
        return render(request,'service/list.htm',{'context': context, 'services' : services})
    except e:
        print(e)
        return redirect('/lab/dashboard/')

@login_required
def detailService(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'My Service',
                }
            
        service = Service.objects.get(id=id)
        
        return render(request,'service/detail.htm', {'context' : context, 'service' : service})
    except:

        return redirect('/lab/dashboard/')


    
@login_required
@transaction.atomic
def updateMicrobiology(request,id):
    print(id)
    object   = Service.objects.get(id=id) 
    form     = MicrobiologyForm(instance=object, data=request.POST or None)

    if form.is_valid():
        try : 
            form.save()
            return redirect('/lab/dashboard/')
        except:
            return redirect('/lab/dashboard/')

    return render(request,'service/updatemicrobiology.htm', {'form' : form, 'service':object})

@login_required
@transaction.atomic
def updateChemistry(request,id):
    object   = Service.objects.get(id=id) 
    form     = ChemistryForm(instance=object,data=request.POST or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
            return redirect('/lab/dashboard/')
        except:

            return redirect('/lab/dashboard/')

    return render(request,'service/updatechemistry.htm', {'form' : form, 'service':object})

@login_required
@transaction.atomic
def updateHematology(request,id):
    object   = Service.objects.get(id=id) 
    form     = HematologyForm(instance = object, data=request.POST or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
            return redirect('/lab/dashboard/')
        except :
            return redirect('/lab/dashboard/')

    return render(request,'service/updatehematology.htm', {'form' : form, 'service':object})

@login_required
@transaction.atomic
def updateBloodBank(request,id):
    object   = Service.objects.get(id=id) 
    form     = BloodBankForm(instance = object, data=request.POST or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
            return redirect('/lab/dashboard/')
        except :
            return redirect('/lab/dashboard/')

    return render(request,'service/updatebloodbank.htm', {'form' : form, 'service':object})

@login_required
@transaction.atomic
def updateMolecularDiagnotics(request,id):
    object   = Service.objects.get(id=id) 
    form     = MolecularDiagnoticsForm(instance = object, data=request.POST or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
            return redirect('/lab/dashboard/')
        except :
            return redirect('/lab/dashboard/')

    return render(request,'service/updatemoleculardiagnotics.htm', {'form' : form, 'service':object})

@login_required
@transaction.atomic
def updateReproductiveBiology(request,id):
    object   = Service.objects.get(id=id) 
    form     = ReproductiveBiologyForm(instance = object, data=request.POST or None)

    if form.is_valid():
        try : 
            main    = True
            form.save()
            return redirect('/lab/dashboard/')
        except :
            return redirect('/lab/dashboard/')

    return render(request,'service/updatereproductivebiology.htm', {'form' : form, 'service':object})




@login_required  
def deleteService(request,id):
    try : 
        Service.objects.filter(id=id).delete()

        return redirect('/lab/dashboard/')
    except:
        return redirect('/lab/dashboard/')    


@login_required
def bookService(request):
    try :
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Shop',
                }

        return render(request,'service/shop.htm',{'context': context})
    except:
        return redirect('/customer/dashboard/')

@login_required
def bookServiceDetail(request,id):
    try:
        context={
                'topic':'Dashboard',
                'account': 'Home',
                'recent_page': 'Service Detail',
                }

        service = Service.objects.get(id=id)

        return render(request,'lab/customer_detail.htm', {'context' : context,'service': service})
    except:
        return redirect('/lab/dashboard/')


@transaction.atomic
@login_required
def uploadReport(request,id):
    object = Appointment.objects.get(id=id)
    form = LabReportForm(instance=object, data=request.POST or None)
    report_file = UploadFileForm(request.POST,request.FILES)

    if request.method == 'POST':    
        if form.is_valid() and report_file.is_valid():
            try:
                Appointment.objects.filter(id=id).update(
                    appointment = request.POST.get('appointment')
                )

                if bool(request.FILES.get('file')) :
                    file = report_file.save(commit=False)
                    file.appointment=object
                    file.save()

                    Appointment.objects.filter(id=id).update(
                        has_file = True
                    )

                return redirect('/lab/appointment/')
            except e:
                print(e)
                return render(request,'service/uploadreport.htm')
    return render(request, 'service/uploadreport.htm', {'form' : form, 'report_file' : report_file, 'id' : id})

@login_required
@transaction.atomic
def bookAppointment(request,id):
    object = Customer.objects.get(user=request.user)
    form = AppointmentForm(request.POST or None)

    if form.is_valid():
        try: 
            main = True
            service = Service.objects.get(id=id)
            appointment = form.save(commit=False)
            appointment.customer = Customer.objects.get(user=request.user)
            appointment.service = Service.objects.get(id=id)
            appointment.lab = Lab.objects.get(id=service.lab.id)
            appointment.save()

            return redirect('/customer/appointment/')
        except e:
            print(e)
            return redirect('/customer/appointment/')
            
    return render(request,'service/appointmentform.htm', {'form' : form, 'id' : id})


@login_required
@transaction.atomic
def pdfList(request):
    files = LabAppointment.objects.all()

    return render (request,'service/pdfList.htm',{'files' : files})
