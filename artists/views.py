from django.shortcuts import render,redirect
from artists.forms import ArtistForm
# Create your views here.
def form(request):
    if(request.method=='POST'):
        my_form=ArtistForm(request.POST)
        if(my_form.is_valid()):
            my_form.save()
            return redirect('artist-form')
    else:
        my_form=ArtistForm
    print(my_form)
    context={
        'form':my_form,
        'title':'Artist',
    }
    return render(request,'artists/form.html',context)
