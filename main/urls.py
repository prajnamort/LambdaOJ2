from django.conf.urls import url, include

from main import views


urlpatterns = [
    url(r'^$',
        views.index.main_index, name='index'),
    url(r'^api/', include([
        url(r'^$',
            views.api_utils.api_root),
        url(r'^problems/$',
            views.problem.ProblemList.as_view(), name='problem-list'),
        url(r'^problems/(?P<pk>\d+)/$',
            views.problem.ProblemDetail.as_view(), name='problem-detail'),
        url(r'^submits/$',
            views.submit.SubmitList.as_view(), name='submit-list'),
        url(r'^submits/(?P<pk>\d+)/$',
            views.submit.SubmitDetail.as_view(), name='submit-detail'),
    ])),
]
