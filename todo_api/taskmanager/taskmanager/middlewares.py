from django.shortcuts import redirect
from django.urls import reverse


class RedirectIfNotAuthenticatedMiddleware: # middleware для редиректа на страницу входа, когда пользователь вышел из системы
    def __init__(self, get_response): # __init__ принимает get_response, который представляет следующую middleware или представление в цепочке обработки запроса
        self.get_response = get_response

    def __call__(self, request): # __call__ вызывается при каждом запросе, принимает объект request и возвращает объект response.
        response = self.get_response(request) # запрашиваем следующую middleware или представление в цепочке обработки запроса
        admin_login_url = reverse('admin:login')
        public_paths = [reverse('login'), reverse('register'), admin_login_url] # откуда не надо перенаправлять
        if not request.user.is_authenticated and request.path not in public_paths: # проверка авторизации и нахождения на странице входа
            return redirect(reverse('login'))
        return response
