from django.conf.urls import url
from . import views
#Importamos 
from control.views import login


from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [

	url(r'^$', views.home),
	url(r'login/^$', login, {'template_name': 'account/home.html'}),

	#Indicamos que cuando acceda a la Url: administrador -> traiga la vista AdministradorList
	url(r'^administrador$', views.AdministradorList.as_view()),

	#Indicamos que cuando acceda a la Url: administrador-barra-un_numero -> traiga la Vista AdministradorDeatil
	url(r'^administrador/(?P<pk>[0-9]+)$', views.AdministradorDetails.as_view()),

	url(r'^director$', views.DirectorList.as_view()),
	url(r'^director/(?P<pk>[0-9]+)$', views.DirectorDetails.as_view()),
	url(r'^maestro$', views.MaestroList.as_view()),
	url(r'^maestro/(?P<pk>[0-9]+)$', views.MaestroDetails.as_view()),
	url(r'^alumno$', views.AlumnoList.as_view()),
	url(r'^alumno/(?P<pk>[0-9]+)$', views.AlumnoDetails.as_view()),
	url(r'^clase$', views.ClaseList.as_view()),
	url(r'^clase/(?P<pk>[0-9]+)$', views.ClaseDetails.as_view()),
	url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]

