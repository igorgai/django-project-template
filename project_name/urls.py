"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    # This is only needed when using runserver.
    urlpatterns = \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
        + urlpatterns

    # # urls for testing error pages locally
    # from django.views.defaults import page_not_found, server_error
    #
    # errors_testing_patterns = [
    #     # url(r'^400/$', TemplateView.as_view(template_name='400.html')),
    #     # url(r'^403/$', TemplateView.as_view(template_name='403.html')),
    #     url(r'^404/$', page_not_found),
    #     url(r'^500/$', server_error),
    # ]
    #
    # urlpatterns += [
    #     url(r'^test-error/', include(errors_testing_patterns)),
    # ]

    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            path(r'^__debug__/', include(debug_toolbar.urls)),
        ]
