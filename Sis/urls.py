from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'sis'
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.Forms.as_view(), name='form'),
    path('list', views.Formlist, name='list'),
    path('detail/<id>', views.detail, name='detail')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
