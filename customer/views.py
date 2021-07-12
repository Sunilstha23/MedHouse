from django.shortcuts import render,redirect
from customer.models import Customer
from django.http import Http404


# Create your views here.
def dashboard(request):
    return render(request, 'customer/dashboard.htm')

def signin(request):
    return render(request, 'customer/signin.htm')

def order(request):
    return render(request, 'customer/order.htm')

def address(request):
    return render(request, 'customer/address.htm')

def profileDetails(request):
    return render(request, 'customer/profile-details.htm')

def forgetPassword(request):
    return render(request, 'customer/forget-password.htm')
def signin(request):
    if request.method == "POST":
        n = request.POST.get("name")
        e = request.POST.get("email")
        p = request.POST.get("password")
        g = request.POST.get("gender")
        print(n, e, p, g)
        try:
            user = Customer.objects.create(
                email=e, name=n, password=p, gender=g)
            print('user.......', user)
            user.save()
            return redirect(login)

        except:
            return render(request, 'signin.htm', {'message': 'Either something went wrong or you did not enter all the required fields.'})
    else:
        return render(request, 'signin.htm')    

def login(request):
    if request.method == "POST":

        e = request.POST.get("email")
        p = request.POST.get("password")

        if e == '' or p == '':
            return render(request, 'login.htm', {'message': "Please enter email or password"})

        else:

            print(e, p)
            try:
                user = Customer.objects.filter(email=e, password=p)

                if user.count() > 0:
                    for user in user:
                        request.session['email'] = user.email
                        request.session['id'] = user.id
                        request.session['name'] = user.name
                        request.session['gender'] = user.gender
                        return redirect('home')
                else:
                    return render(request, 'login.htm', {'message': "Your email or password might be wrong."})
            except:
                return render(request, 'login.htm', {'message': "Something went wrong. Please try to login again!"})
    else:
        return render(request, 'login.htm')

def logout(request):
    request.session.flush()
    return redirect('index')

# 
