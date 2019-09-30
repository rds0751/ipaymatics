from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from .views import home,tree_view,index,profile_view,admin_dashboard_view,admin_dashboard_view_single,edit_profile_view,withdrwal

from accounts.views import refer_view

urlpatterns = [
path('admin/', admin.site.urls),
path('home', home),
path('', index),
path('tree/', tree_view, name='tree'),
path('refer/', refer_view, name='refer'),
path('myprofile/', profile_view, name='myprofile'),
path('myprofile/edit', edit_profile_view, name='edit'),
path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
path('admin_dashboard/profile/<int:myid>', admin_dashboard_view_single),
path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
path('order/', include(('order.urls', 'order'), namespace='order')),
path('contact/', include('contact.urls')),
path('accounts/', include('accounts.urls')),
path('ckeditor/', include('ckeditor_uploader.urls')),
path('withdrwal/', withdrwal),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

