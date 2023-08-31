# from django.urls import path
# from navi import views
# from django.contrib import admin 

# app_name = 'navi'

# urlpatterns = [
#     path('', views.testdata, name='testdata_view'),
# ]
from django.contrib import admin
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('navi.urls')),
# ]

# from django.contrib import admin
# from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('testcase.urls', namespace='testcase')),  # Add namespace here
    # path('navi/', include('navi.urls')),
]
