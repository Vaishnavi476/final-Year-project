from django.urls import path
from .views import homeview, welcomeview, ordering, view_hr, detail_hr, purchase, rent, equipment, user_profileview
from .views import service_request, edit_profileview, contact
from .views import index
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('', homeview, name='home'),
    path('welcome/',welcomeview, name='welcome'),
    path('ordering/',ordering,name='ordering'),
    path('hr/view',view_hr, name='view_hr'),
    path('hr/detail/<int:pk>',detail_hr, name='detail_hr'),
    path('purchase/',purchase, name='pc'),
    path('rent/',rent, name='rs'),
    path('service/request/<int:pk>',service_request, name='sr'),
    path('equipment/',equipment, name='eq'),
    path('userprofile/', user_profileview, name='up'),
    path('editprofile/<int:pk>', edit_profileview, name='editpro'),
    path('',index,name='home'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('product/detail/<int:pk>',views.show_single_product,name='product_detail'),
    path('product/all',views.show_products,name='product_all'),
    path('contact/',contact, name='contact'),
    path("config/",views.stripe_config, name='config'),
    path('create-checkout-session/',views.create_checkout_session,name='create_checkout_session'),
    path('success/',views.notify_success,name='success'),
    path('cancelled/',views.notify_cancelled,name='cancelled'),
    path('feedback/',views.feedback, name='feedback'),
    path("about/",TemplateView.as_view(template_name='about.html'),name='about')
]


