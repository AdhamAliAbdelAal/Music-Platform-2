from django.shortcuts import render,redirect
from albums.forms import AlbumForm
# Create your views here.
def form(request):
    if(request.method=='POST'):
        my_form=AlbumForm(request.POST)
        if(my_form.is_valid()):
            my_form.save()
            return redirect('artist-form')
    else:
        my_form=AlbumForm
    print(my_form)
    context={
        'form':my_form,
        'title':'Album',
    }
    return render(request,'albums/form.html',context)
