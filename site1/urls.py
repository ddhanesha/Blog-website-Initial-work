from django.conf.urls import url,patterns

from site1.views import post_list

urlpatterns = patterns('',
        url(r'^post_list/', post_list),
)