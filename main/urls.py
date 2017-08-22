from django.conf.urls import url, include

from main import views


urlpatterns = [
    url(r'^$',
        views.index.main_index, name='index'),

    url(r'^swagger/$',
        views.api_utils.swagger_view, name='swagger'),
    url(r'^swagger.json$',
        views.api_utils.swagger_json, name='swagger_json'),

    url(r'^api/', include([
        url(r'^$',
            views.api_utils.api_root, name='api_root'),

        url(r'^auth/login/$',
            views.auth.LoginView.as_view(), name='auth-login'),
        url(r'^auth/logout/$',
            views.auth.LogoutView.as_view(), name='auth-logout'),
        url(r'^auth/password/$',
            views.auth.SetPasswordView.as_view(), name='auth-password'),

        url(r'^problems/$',
            views.problem.ProblemList.as_view(), name='problem-list'),
        url(r'^problems/(?P<number>\d+)/$',
            views.problem.ProblemDetail.as_view(), name='problem-detail'),
        url(r'^submits/$',
            views.submit.SubmitList.as_view(), name='submit-list'),
        url(r'^submits/(?P<pk>\d+)/$',
            views.submit.SubmitDetail.as_view(), name='submit-detail'),

        url(r'^my/info/$',
            views.user.MyInfo.as_view(), name='my-info'),
        url(r'^my/submits/$',
            views.user.MySubmitList.as_view(), name='my-submit-list'),
    ])),
]
