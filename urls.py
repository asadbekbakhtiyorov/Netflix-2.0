from django.contrib import admin
from django.urls import path, include
from film.views import Home, ActorAPI, MovieAPI
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Netfix API",
      default_version='v1',
      description="Netflix2.0, or clone for testing API",
      contact=openapi.Contact(email="asadbekbakhtiyorov76@mail.ru"),
   ),
   public=True,
)


router = DefaultRouter()
router.register('movie', MovieAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', Home.as_view()),
    path('actor/', ActorAPI.as_view()),
    path('actor/<int:pk>/', ActorAPI.as_view()),
    path('', include(router.urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_doc'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc')
]
