from django.contrib.auth import views as av
from django.urls import path
from . import views as v
urlpatterns = [
    path("", v.home, name="home"), path("mashq/", v.mashq, name="mashq"), path("api/matn/", v.matn_api, name="matn_api"),
    path("api/natija/", v.saqlash, name="saqlash"), path("reyting/", v.reyting, name="reyting"),
    path("natijalarim/", v.natijalarim, name="natijalarim"), path("sozlamalar/", v.sozlamalar, name="sozlamalar"),
    path("kirish/", av.LoginView.as_view(template_name="core/kirish.html"), name="login"),
    path("chiqish/", av.LogoutView.as_view(), name="logout"), path("royxatdan-otish/", v.royxat_form, name="royxat"),
]
