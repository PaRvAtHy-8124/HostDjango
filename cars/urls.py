from django.urls import path
from . import views
app_name='cars'
urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('images/',views.images,name='images'),
    path('home/<int:id>',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    path('gallerys/',views.gallerys,name='gallerys'),
    path('detail/<int:id>',views.detail,name='detail'),
]