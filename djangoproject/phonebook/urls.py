from django.urls import path
from djangoproject.phonebook.views import create_contact, landing_page

urlpatterns = [
    path('', landing_page, name='langing-page'),
    path('new-contact', create_contact, name = 'new-contact'),
]