from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from . import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('userapp.urls', namespace='userapp')),
                  path('groupsapp/', include('groupapp.urls', namespace='groupapp')),
                  path('auth_api/', include('api.apiauthapp.urls')),
                  path('', include('api.apiuserapp.urls')),
                  path('', include('api.apigroupapp.urls')),
                  path('', include('api.apichatapp.urls')),
                  path('', include('api.apitaskapp.urls')),
                  path('', include('api.apieventapp.urls')),
                  path('', include('api.apishopingapp.urls')),
                  path('docs/', include('api.apidocs.urls')),
                  path('auth/', include('authapp.urls', namespace='auth')),
                  path('groupsapp/<group_pk>/shoppingapp/', include('shoppingapp.urls', namespace='shop')),
                  path('groupsapp/<group_pk>/chatapp/', include('chatapp.urls', namespace='chatapp')),
                  path('groupsapp/<group_pk>/tasks/', include('taskapp.urls', namespace='taskapp')),
                  path('groupsapp/<group_pk>/eventsapp/', include('eventapp.urls', namespace='eventapp')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
