from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns =[
path('',views.inicio,name='inicio'), 
path('nosotros',views.nosotros,name='nosotros'), 
path('ayuda',views.ayuda,name='ayuda'),
path('productos',views.productos,name='productos'), 
path('productosAdmin',views.productosAdmin,name='productosAdmin'), 
path('anadirProducto',views.anadirProducto,name='anadirProducto'),
path('hacerOrden',views.hacerOrden,name='hacerOrden'), 
path('eliminarOrden/<int:id>',views.eliminarOrden,name='eliminarOrden'),
path('eliminarProducto/<int:id>',views.eliminarProducto,name='eliminarProducto'),
path('editarProducto/<int:id>',views.editarProducto,name='editarProducto'),
path('login',LoginView.as_view(template_name='login.html'),name='login'),
path('logout',LogoutView.as_view(template_name='logout.html'),name='logout'),
path('ordenes',views.ordenes,name='ordenes'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)