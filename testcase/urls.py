from django.urls import path
from testcase import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'testcase'

urlpatterns = [ 
    
    path('', views.index, name='index'),
    path('delete/<int:data_id>/', views.delete, name='delete'),
    path('update/<int:data_id>/', views.update, name='update'),
    path('filter/', views.filter, name='filter'),
    path('download/', views.download, name='download'),
    path('add/', views.add, name='add'),
    path('download-csv/', views.download_csv, name='download-csv'),
    path('download_full_csv/', views.download_full_csv, name='download_full_csv'),
    path('summary/', views.summary, name='summary'), 
    path('summary1/', views.summary1, name='summary1'), 
    path('summary2/', views.summary2, name='summary2'),
    path('get-dropdown-options/', views.get_dropdown_options, name='get_dropdown_options'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)