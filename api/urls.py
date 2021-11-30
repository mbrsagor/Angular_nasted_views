from django.urls import path
from api.nominaiton_api import SymbolListAPIView, ListOfNominationView

urlpatterns = [
    path('symbol/', SymbolListAPIView.as_view()),
    path('nominaiton', ListOfNominationView.as_view())
]
