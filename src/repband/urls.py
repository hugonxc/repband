from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),

    path('user/signup', views.signup , name='signup'),
    path('user/logout', views.logout_view , name='logout'),

    path('account/profile', views.profile , name='profile'),


    # path('repertory/create', views.create_repertory , name='create_repertory'),
    # path('repertory/manage', views.manage_repertory , name='manage_repertory'),
    # path('repertory/add_music', views.add_music , name='add_music'),    

    path('repertory/add_new_music', views.add_new_music , name='add_new_music'),

]
