from django.conf.urls import url, include
from django.contrib import admin
 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('personal.urls')),
    url(r'^blogs/', include('blogs.urls')),
    url(r'^ngos/', include('ngos.urls')),
    url(r'^aboutus/', include('aboutus.urls')),
    url(r'^Mission/', include('Mission.urls')),
    url(r'^partners/', include('partners.urls')),
    url(r'^cities/', include('cities.urls')),
    url(r'^work/', include('work.urls')),
    url(r'^contributions/', include('contributions.urls')),
     url(r'^team/', include('team.urls')),
     
     
     
    
]
