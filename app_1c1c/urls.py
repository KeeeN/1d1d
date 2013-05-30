from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone

from sondages.models import Poll

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Poll.objects.filter(pub_date__lte=timezone.now) \
            .order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='sondages/index.html'),
        name='index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            queryset=Poll.objects.filter(pub_date__lte=timezone.now),
            model=Poll,
            template_name='sondages/detail.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Poll,
            template_name='sondages/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'sondages.views.vote', name='vote'),
)