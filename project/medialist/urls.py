from django.conf.urls import patterns, url

from medialist import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^user/(?P<slug>\w+)$', views.profile, name='profile'),

    url(r'^$', views.MediaList.as_view(), name='media_list'),
    url(r'^(?P<slug>\w+)/$', views.MediaDetail.as_view(), name='media_detail'),
    url(r'^media/new$', views.MediaCreate.as_view(), name='media_create'),

    url(r'^(?P<slug>\w+)/edit/(?P<field>\w+)$', views.MediaUpdate.as_view(), name='media_update'),

    url(r'^(?P<slug>\w+)/journalist$', views.JournalistCreate.as_view(), name='journalist_create'),

    url(r'^(?P<slug>\w+)/(?P<journalist>[-\w]+)/$', views.JournalistDetail.as_view(), name='journalist_detail'),
    url(r'^(?P<slug>\w+)/(?P<journalist>[-\w]+)/edit/(?P<field>\w+)$', views.JournalistUpdate.as_view(), name='journalist_update'),

    url(r'^(?P<slug>\w+)/(?P<journalist>[-\w]+)/article$', views.JournalistArticleCreate.as_view(), name='journalist_article_create'),
)
