from django.conf.urls import url, include

from djoser import views as djoser_views

from main import views


urlpatterns = [
    url(r'^$',
        views.index.main_index, name='index'),
    url(r'^api/', include([
        url(r'^$',
            views.api_utils.api_root),

        url(r'^auth/login/$',
            djoser_views.LoginView.as_view(), name='auth_login'),
        url(r'^auth/logout/$',
            djoser_views.LogoutView.as_view(), name='auth_logout'),
        url(r'^auth/password/$',
            djoser_views.SetPasswordView.as_view(), name='auth_password'),

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
    ])),
]
