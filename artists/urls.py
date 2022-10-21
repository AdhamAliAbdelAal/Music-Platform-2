from artists import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.artists,name='artists'),
    path('create', views.form,name='artist-form'),
]

urlpatterns += staticfiles_urlpatterns()