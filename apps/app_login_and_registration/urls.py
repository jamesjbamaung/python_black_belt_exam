from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^successful_login$', views.successful_login),
    url(r'^log_out$', views.log_out),
    url(r'^my_account/(?P<user_id>\d+)$', views.my_account),
    url(r'^posted_by_user/(?P<quote_user_id>\d+)$', views.posted_by),
    url(r'^edit_account$', views.edit_account),
    
]