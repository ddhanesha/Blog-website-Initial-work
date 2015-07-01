from django.conf.urls import url,patterns

from site1.views import post_list,post_detail

urlpatterns = patterns('',
        url(r'^post_list/', post_list),
        url(r'post_detail/(?P<pk>[0-9]+)/',post_detail),
)