from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Order, OrderItem, Coupon
from .forms import CartAddForm, CouponApplyForm
from .cart import Cart
from education.models import Education
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


# Create your views here.

class OrderingView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'ordering/list.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, education_id):
        cart = Cart(request)
        education = get_object_or_404(Education, id=education_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(education, form.cleaned_data['quantity'])
        return redirect('ordering:cart')


class CartRemoveView(View):
    def get(self, request, education_id):
        cart = Cart(request)
        education = get_object_or_404(Education, id=education_id)
        cart.remove(education)
        return redirect('ordering:cart')


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order,
                                     education=item['education'],
                                     quantity=item['quantity'],
                                     price=item['price'])
        cart.clear()
        return redirect('ordering:order_detail', order.id)


class OrderDetailView(LoginRequiredMixin, View):
    form_class = CouponApplyForm

    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'ordering/detail.html', {'order': order,
                                                        'form': self.form_class})


class ApplyCouponView(LoginRequiredMixin, View):
    form_class = CouponApplyForm

    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = self.form_class(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_form__lte=now, valid_form__gte=now, active=True)
            except Coupon.DoesNotExist:
                messages.error(request, 'کد نامعتبر است !' , 'danger')
                return redirect('ordering:order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
        return redirect('ordering:order_detail', order_id)



