from django.urls import path
from .views import signUpView
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',signUpView, name='signup'),
    path('home/', include('events.urls', namespace='events')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
