from django.conf.urls import url
from api import views

urlpatterns = [
  
    url(r'^addresses/(?P<id>[0-9]+)$', views.AddressesAPIView.as_view()),
    url(r'^addresses/$', views.AddressesAPIListView.as_view()),
  
    url(r'^budgetsituations/(?P<id>[0-9]+)$', views.BudgetSituationsAPIView.as_view()),
    url(r'^budgetsituations/$', views.BudgetSituationsAPIListView.as_view()),
  
    url(r'^budgets/(?P<id>[0-9]+)$', views.BudgetsAPIView.as_view()),
    url(r'^budgets/$', views.BudgetsAPIListView.as_view()),
  
    url(r'^clients/(?P<id>[0-9]+)$', views.ClientsAPIView.as_view()),
    url(r'^clients/$', views.ClientsAPIListView.as_view()),
  
    url(r'^migrations/(?P<id>[0-9]+)$', views.MigrationsAPIView.as_view()),
    url(r'^migrations/$', views.MigrationsAPIListView.as_view()),
  
    url(r'^registrationsituations/(?P<id>[0-9]+)$', views.RegistrationSituationsAPIView.as_view()),
    url(r'^registrationsituations/$', views.RegistrationSituationsAPIListView.as_view()),
  
    url(r'^serviceproviders/(?P<id>[0-9]+)$', views.ServiceProvidersAPIView.as_view()),
    url(r'^serviceproviders/$', views.ServiceProvidersAPIListView.as_view()),
  
    url(r'^servicetypes/(?P<id>[0-9]+)$', views.ServiceTypesAPIView.as_view()),
    url(r'^servicetypes/$', views.ServiceTypesAPIListView.as_view()),
  
    url(r'^services/(?P<id>[0-9]+)$', views.ServicesAPIView.as_view()),
    url(r'^services/$', views.ServicesAPIListView.as_view()),
  
    url(r'^usertypes/(?P<id>[0-9]+)$', views.UserTypesAPIView.as_view()),
    url(r'^usertypes/$', views.UserTypesAPIListView.as_view()),
  
    url(r'^users/(?P<id>[0-9]+)$', views.UsersAPIView.as_view()),
    url(r'^users/$', views.UsersAPIListView.as_view()),
  
  ]
