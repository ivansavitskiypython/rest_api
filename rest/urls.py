from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from article import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('posts', views.ArticleViewSet)
router.register('my_posts', views.UserArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
