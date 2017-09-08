from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from article import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, 'users')
router.register(r'posts', views.ArticleViewSet, 'posts')
router.register(r'my_posts/import_xml', views.ImportXMLViewSet)
router.register(r'my_posts', views.UserArticleViewSet, 'my_posts')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
