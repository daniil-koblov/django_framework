from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:client_id>', views.orders, name='orders'),
    path('orders/', views.orders, name='all_orders'),
path('__debug__/', include("debug_toolbar.urls")),
]