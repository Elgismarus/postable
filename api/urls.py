from django.urls import path
from .views import PostalCodeDetailView

urlpatterns = [
    path('postalcode/<str:country>/<str:code>', PostalCodeDetailView.as_view())
]
