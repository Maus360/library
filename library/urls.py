from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from main_app import views

router = routers.DefaultRouter(trailing_slash=True)
router.register(r"person", views.PersonViewSet)
router.register(r"book", views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns += router.urls
