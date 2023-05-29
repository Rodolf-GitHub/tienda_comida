from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request,'index.html')

def nosotros(request):
    return render(request, 'nosotros.html')
def ayuda(request):
    return render(request, 'ayuda.html')
#-------------------------Productos-------------------------
def productos(request):
    productos=Producto.objects.all()
    return render(request, 'productos.html',{'productos':productos})
@login_required
def productosAdmin(request):
    productos=Producto.objects.all()
    return render(request, 'admin/productosAdmin.html',{'productos':productos})
@login_required
def anadirProducto(request):
    formulario=ProductoForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productosAdmin')
    else: print('Error')
    return render(request, 'admin/anadirProducto.html',{'formulario':formulario})
@login_required
def eliminarProducto(request,id):
    usuarios=Producto.objects.get(id=id)
    usuarios.delete(using='default')
    return redirect('productosAdmin')
@login_required
def editarProducto(request,id):
    notas=Producto.objects.get(id=id)
    formulario=ProductoForm(request.POST or None,request.FILES or None,instance=notas)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('productosAdmin')
    return render(request,'admin/editarProducto.html',{'formulario':formulario})
#----------------------------ordenes--------------------
@login_required
def ordenes(request):
    ordenes=Orden.objects.all()
    return render(request, 'ordenes.html',{'ordenes':ordenes})
def hacerOrden(request):
    formulario=OrdenForm(request.POST or None,request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    else: 
        
        print('Error')
    return render(request, 'hacerOrden.html',{'formulario':formulario})
@login_required
def eliminarOrden(request,id):
    usuarios=Orden.objects.get(id=id)
    usuarios.delete()
    return redirect('ordenes')
    #---------------------------registro usuario---------------------------

