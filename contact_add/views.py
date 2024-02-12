from django.shortcuts import render, redirect
from contact_add.models import user, add_user

# Create your views here.


def home(request):
    msg = ''
    if 'user_id' in request.session:
        return redirect('/deshbord')
    if 'login' in request.POST:
        email = request.POST['email']
        password = request.POST['password']
        obj = user.objects.filter(email=email, password=password)
        if obj.count() == 1:
            print('succes')
            row = obj.get()
            request.session['user_id'] = row.id

            return redirect("deshbord/")
        else:
            print('failer')
            msg = "Invalid emial ar password"
    return render(request, 'index.html', {'msg': msg})


def register(request):
    s = ' '
    if 'login' in request.POST:
        a_name = request.POST['name']
        a_email = request.POST['email']
        a_password = request.POST['password']

        obj = user(
            name=a_name,
            email=a_email,
            password=a_password
        )
        obj.save()
        print("Suscces")
        return redirect('/', {'obj': obj})
    return render(request, 'register.html')


def view_user(request):
    cont = user.objects.all()
    return render(request, 'view_user.html', {'cont': cont})


def deshbord(request):
    if 'user_id' not in request.session:
        return redirect('/')
    # obj = add_user.objects.all()
    id = request.session['user_id']
    obj = user.objects.filter(id=id)
    obj2 = add_user.objects.filter(add_by=id)
    row = obj.get()
    # print(user_id)
    return render(request, 'deshbord.html', {'user': row.name, 'obj': obj2, 'id': id})


def logout(request):
    del request.session['user_id']
    return redirect('/')


def contact_add(request):

    return render(request, 'contact_add.html')


def add_cant(request):
    print("Succes1")
    if 'add' in request.POST:
        name = request.POST['nm']
        email = request.POST['em']
        password = request.POST['pas']
        contact = request.POST['cnt']
        city = request.POST['ct']
        gender = request.POST['gn']

        obj = add_user(
            add_by=request.session['user_id'],
            name=name,
            email=email,
            password=password,
            Contact=contact,
            City=city,
            Gender=gender,

        )
        print("Succes2")
        obj.save()
        return redirect('/deshbord')
    return render(request, 'contact_add.html')


def delete_data(request, del_id):
    print("del ===", del_id)
    add_user.objects.filter(id=del_id).delete()
    return redirect('/deshbord')


def edit_data(request, edit_id):
    obj = add_user.objects.filter(id=edit_id).get()
    if 'add' in request.POST:
        name = request.POST['nm']
        email = request.POST['em']
        password = request.POST['pas']
        contact = request.POST['cnt']
        city = request.POST['ct']
        gender = request.POST['gn']
        obj.name = name
        obj.email = email
        obj.password = password

        obj.Contact = contact
        obj.City = city
        obj.Gender = gender
        obj.save()
        return redirect('/deshbord')
    return render(request, 'contact_add.html', {'obj': obj})


def edit_pro(request, edit_pro):
    obj = user.objects.filter(id=edit_pro).get()
    if 'login' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        obj.name = name
        obj.email = email
        obj.password = password
        obj.save()
        return redirect('/deshbord')
    return render(request, 'register.html', {'obj': obj})
