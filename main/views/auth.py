from djoser import views as djoser_views


class LoginView(djoser_views.LoginView):
    throttle_scope = 'auth-login'


class LogoutView(djoser_views.LogoutView):
    pass


class SetPasswordView(djoser_views.SetPasswordView):
    throttle_scope = 'auth-password'
