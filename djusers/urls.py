from django.contrib import admin
from django.urls import path,include

from .views import home,tree_view,index

from accounts.views import login_view, register_view, logout_view

urlpatterns = [
path('admin/', admin.site.urls),
path('home', home),
path('', index),
path('tree/', tree_view, name='tree'),
path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
path('order/', include(('order.urls', 'order'), namespace='order')),

path('contact/', include('contact.urls')),
path('accounts/login/', login_view),
path('accounts/register/', register_view),
path('accounts/logout/', logout_view),
path('ckeditor/', include('ckeditor_uploader.urls')),
]
