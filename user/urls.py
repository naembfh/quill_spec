from django.urls import path
from .views import registration_view,logout_view,login_view,edit_profile_view

urlpatterns = [
    path('register/',registration_view,name='registration'),
     path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('edit_profile/', edit_profile_view, name='edit_profile')

]
