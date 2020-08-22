from django.conf.urls import url
from appointment import views

urlpatterns = [
    url(r'^api/schedule$', views.appointment),
    url(r'^api/appointment$', views.appointment_match),
    url(r'^api/scheduled$', views.scheduled)
]