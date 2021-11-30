from django.urls import path
from api.nominaiton_api import ListOfNominationView

urlpatterns = [
    path('nominaiton', ListOfNominationView.as_view())
]
