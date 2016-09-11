from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from polls import views

router = routers.DefaultRouter()
router.register('questions', views.QuestionViewSet)

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
