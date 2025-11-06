from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Soriana, name='inicio_soriana'),
    path('empleados/', views.ver_Empleados, name='ver_empleados'),
    path('empleados/agregar/', views.agregar_Empleado, name='agregar_empleado'),
    path('empleados/actualizar/<int:pk>/', views.actualizar_Empleado, name='actualizar_empleado'),
    path('empleados/realizar_actualizacion/<int:pk>/', views.realizar_actualizacion_Empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:pk>/', views.borrar_Empleado, name='borrar_empleado'),
]