from django.contrib import admin
from django.urls import path

app_name = "root_app"
urlpatterns = [
    path("admin/", admin.site.urls),
]

# handler400 = "root.views.not_found"

# handler500 = "root.views.interval_error"
