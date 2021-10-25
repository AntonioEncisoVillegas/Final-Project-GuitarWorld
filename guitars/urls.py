from django.urls import path
from guitars import views
urlpatterns = [
    path('guitars/by/brand/<int:id>', views.guitarsByBrand, name="guitars-by-brand"),
    path('guitar/comercial/info/<int:id>', views.guitarInformation, name="guitarComercial-info"),
    path('guitars/handmade/', views.allHandMadeGuitars, name="all-handmade"),
    path('guitar/handmade/info/<int:id>', views.guitarInformationHandMade, name="handmade-info"),
    path('guitars/handmade/by/country/<int:id>', views.guitarsByCountry, name="by-country"),
    path('punctuate/comercial/<int:id>', views.punctuateComercial, name="punctuate-comercial"),
    path('punctuate/handMade/<int:id>', views.punctuateHandMade, name="punctuate-handMade"),
    path('guitars/by/search/', views.guitarBySearch, name="guitar-by-search")
]