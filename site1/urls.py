from django.conf.urls import url,patterns

from site1.views import post_list,post_detail,post_new,post_edit,registration

urlpatterns = patterns('',
        url(r'^registration/',registration),
        url(r'^post_list/', post_list),
        url(r'^post_detail/(?P<pk>[0-9]+)/',post_detail,name="post_detail"),
        url(r'^post_new/',post_new),
        url(r'^post_edit/(?P<pk>[0-9]+)/',post_edit, name="post_edit"),
)