from django.shortcuts import render,redirect
from artists.forms import ArtistForm
from artists.models import Artist
# Create your views here.
def form(request):
    if(request.method=='POST'):
        my_form=ArtistForm(request.POST)
        if(my_form.is_valid()):
            my_form.save()
            return redirect('artists')
    else:
        my_form=ArtistForm
    #print(my_form)
    context={
        'form':my_form,
        'title':'Artist Form',
    }
    return render(request,'artists/form.html',context)

def artists(request):
    def get_all_artists():
        all_artists=Artist.objects.all()
        return [(artist,artist.album_set.all()) for artist in all_artists ]
    data=get_all_artists()
    print(data)
    context={
        'data':data,
    }
    return render(request,'artists/artists.html',context)
