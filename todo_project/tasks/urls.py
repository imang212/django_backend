from django.urls import path
from .views import Vrat_seznam_ukolu, Vloz_ukol

urlpatterns = [
    path("tasks/", Vrat_seznam_ukolu, name="task-list"),
    path("tasks/", Vloz_ukol, name="task-create"),
]
