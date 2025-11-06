from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from django.contrib import messages

# Función para la página de inicio
def inicio_Soriana(request):
    return render(request, 'inicio.html')

# Función para agregar un nuevo empleado
def agregar_Empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_contratacion = request.POST.get('fecha_contratacion')
        puesto = request.POST.get('puesto')
        salario = request.POST.get('salario')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')

        try:
            Empleado.objects.create(
                nombre=nombre,
                apellido=apellido,
                fecha_contratacion=fecha_contratacion,
                puesto=puesto,
                salario=salario,
                email=email,
                telefono=telefono
            )
            messages.success(request, '¡Empleado agregado exitosamente!')
            return redirect('ver_empleados')
        except Exception as e:
            messages.error(request, f'Error al agregar empleado: {e}')
            return render(request, 'Empleados/agregar_empleados.html')
    return render(request, 'Empleados/agregar_empleados.html')

# Función para ver todos los empleados
def ver_Empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'Empleados/ver_empleados.html', {'empleados': empleados})

# Función para mostrar el formulario de actualización de un empleado
def actualizar_Empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request, 'Empleados/actualizar_empleados.html', {'empleado': empleado})

# Función para realizar la actualización de un empleado
def realizar_actualizacion_Empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.apellido = request.POST.get('apellido')
        empleado.fecha_contratacion = request.POST.get('fecha_contratacion')
        empleado.puesto = request.POST.get('puesto')
        empleado.salario = request.POST.get('salario')
        empleado.email = request.POST.get('email')
        empleado.telefono = request.POST.get('telefono')
        try:
            empleado.save()
            messages.success(request, '¡Empleado actualizado exitosamente!')
            return redirect('ver_empleados')
        except Exception as e:
            messages.error(request, f'Error al actualizar empleado: {e}')
    return render(request, 'Empleados/actualizar_empleados.html', {'empleado': empleado})

# Función para borrar un empleado
def borrar_Empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, '¡Empleado eliminado exitosamente!')
        return redirect('ver_empleados')
    return render(request, 'Empleados/borrar_empleados.html', {'empleado': empleado})
