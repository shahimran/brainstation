from meal import views
from django.conf.urls import url
app_name = 'meal'

urlpatterns = [
    url(r'^menu/',views.menu,name="menu"),
]