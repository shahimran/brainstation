from meal import views
from django.conf.urls import url

app_name = 'meal'

urlpatterns = [
    url(r'^menu/',views.menu,name="menu"),
    url(r'^tokens/',views.token_list,name="token_list"),
    url(r'^registration/',views.registration,name="registration"),
    url(r'^user/',views.user,name="user"),
]