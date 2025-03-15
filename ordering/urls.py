from django.urls import path
from . import views

app_name = 'ordering'
urlpatterns = [
    path('cart/', views.OrderingView.as_view(), name='cart'),
    path('add/<int:education_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<int:education_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('detail/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('apply/<int:order_id>/', views.ApplyCouponView.as_view(), name='apply_coupon'),
]