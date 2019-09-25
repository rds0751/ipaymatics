from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from .views import home,tree_view,index,profile_view,savings_view,admin_dashboard_view

from accounts.views import login_view, register_view, logout_view, refer_view

urlpatterns = [
path('admin/', admin.site.urls),
path('home', home),
path('', index),
path('tree/', tree_view, name='tree'),
path('refer/', refer_view, name='refer'),
path('myprofile/', profile_view, name='myprofile'),
path('admin_dashboard/', admin_dashboard_view, name='admin_dashboard'),
path('mysavings/', savings_view, name='savings_view'),
path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
path('order/', include(('order.urls', 'order'), namespace='order')),
path('contact/', include('contact.urls')),
path('accounts/login/', login_view),
path('accounts/register/', register_view),
path('accounts/logout/', logout_view),
path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

