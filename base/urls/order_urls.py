from unicodedata import name
from django.urls import path 
from base.views import order_views as views




urlpatterns = [
   path('add/',views.addOrderItems,name='orders-add'),
   path('',views.getOrders,name='Orders'),
   path('myorders/',views.getMyOrders,name='myOrders'),
   path('<str:pk>/deliver/',views.updateOrderToDelivered,name='order-delivered'), 
   path('<str:pk>/',views.getOrderById,name='user-order'), 
   path('<str:pk>/pay/',views.updateOrderToPaid,name='pay')
]
 