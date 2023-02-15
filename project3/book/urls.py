from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('osaindex',views.osaindex,name='osaindex'),
    path('first', views.first,name='first'),
    path('second', views.second,name='second'),
    path('third', views.third,name='third'),
    path('ee', views.ee,name='ee'),
    path('eein', views.eein,name='eein'),
    path('eenext', views.eenext,name='eenext'),
    path('eeenext', views.eeenext,name='eeenext'),
    path('osake', views.osake,name='osake'),
    path('osakein', views.osakein,name='osakein'),
    path('osaket', views.osaket,name='osaket'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('user', views.user, name='user'),
    path('new', views.new, name='new'),
    path('choice', views.choice, name='choice'),
    path('content/<int:num>', views.content, name='content'),
    path('post', views.post, name='post'),
    path('start/<int:num>', views.start, name='start'),

]