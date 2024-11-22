from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from students.apps import StudentsConfig

app_name = StudentsConfig.name

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('index/<int:student_id>/', views.index, name='index'),
    path('student_detail/<int:student_id>/', views.student_detail, name='student_detail'),
    path('students/', views.student_list, name='student_list'),
    path('student/create/', views.StudentCreateView.as_view(), name='student_create'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),

    path('mymodel/create/', views.MyModelCreateView.as_view(), name='mymodel_create'),
    path('mymodel/list/', views.MyModelListView.as_view(), name='mymodel_list'),
    path('mymodel/detail/<int:pk>/', views.MyModelDetailView.as_view(), name='mymodel_detail'),
    path('mymodel/update/<int:pk>/', views.MyModelUpdateView.as_view(), name='mymodel_update'),
    path('mymodel/delete/<int:pk>/', views.MyModelDeleteView.as_view(), name='mymodel_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # path('show_data/', views.show_data, name='show_data')]
#     path('submit_data/', views.submit_data, name='submit_data'),
#     path('item/<int:item_id>/', views.show_item, name='show_item')
# ]