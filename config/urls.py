from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView, CreateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from photologue.models import Photo
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("justforfam.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # TinyMVE
    path('tinymce/', include('tinymce.urls')),

    # Houses and Rooms
    path('<username>/', include('justforfam.house.urls')),
    # Blog posts
    path('<username>/home/<house_name>/room/<room_name>/', include('justforfam.posts.urls')),
    # Relations
    path('<username>/join/', include('justforfam.relations.urls')),
    # Photo Gallery
    path('gallery/', include('justforfam.gallery.urls', namespace='gallery')),

    ############
    # 3rd Party
    ############

    # path('photologue/photo/add/', CreateView.as_view(model=Photo, success_url='/', fields=('title', 'caption', 'image',)), name='add-photo'),
    # Photologue
    path('photologue/', include('photologue.urls', namespace='photologue')),
    # Avatar
    path('avatar/', include('avatar.urls')),
    # Comments
    path('comments/', include('django_comments_xtd.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()

# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("auth-token/", obtain_auth_token),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
