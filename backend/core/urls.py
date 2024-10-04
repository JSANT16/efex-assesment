from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerSplitView, SpectacularAPIView
urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerSplitView.as_view(url_name='schema'), name='redoc'),
    path('api/', include('student.urls')),
]
