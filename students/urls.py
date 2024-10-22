from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'students'

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # path('show_data/', views.show_data, name='show_data')]
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item')
# ]