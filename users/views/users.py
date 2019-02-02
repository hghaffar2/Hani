from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from users.models.users import User
from users.forms.users import UserForm
from django.contrib.sessions.models import Session
from users.forms.imageForm import ImageForm
from users.models.photos import Photo
from django.contrib.auth.decorators import login_required



def signup(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("login")

        else:
            return HttpResponse("check data you entered")

    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form':form})


def user_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        user_id = user.pk
        request.session['id'] = user_id

        if user:
            if user.is_active:
                login(request, user)
                return redirect('listing')
            else:
                return HttpResponse("not valid account ")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request,'registration/login.html')


@login_required
def listing(request):

    user_id = request.session['id']

    data = User.objects.get(id=user_id)

    photos = Photo.objects.filter(user=user_id)

    paginator_brands = Paginator(photos,7)
    page_photo = request.GET.get('page')
    all_photos = paginator_brands.get_page(page_photo)

    return render(request,'user/profile.html',{'user':data,'photos':all_photos})


@login_required
def addImg(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ImageForm(request.POST,request.FILES)

            # return HttpResponse(form)

            if form.is_valid():
                img = Photo(picture=request.FILES['picture'], user=request.user)
                img.save()
                return redirect('listing')
            else:
                return HttpResponse('check size of picture you selected its limited')


@login_required
def submitImg(request):

    form = ImageForm()
    return render(request,'user/imageFile.html',{'form':form})













