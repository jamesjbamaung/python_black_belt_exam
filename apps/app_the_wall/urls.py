from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^quotes$', views.quotes),
    url(r'^post_quote$', views.post_quote),
    url(r'^comments$', views.comments),
    url(r'^delete_quote/(?P<quote_id>\d+)$', views.delete_quote),
    url(r'^like_quote/(?P<quote_id>\d+)$', views.like_quote),
    url(r'^like_comment/(?P<comment_id>\d+)$', views.like_comment),
    
]