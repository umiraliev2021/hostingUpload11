"""




"""
from django.contrib import admin
from django.urls import path
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),

    # ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # 
    # ================================================== >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    path('admin-warehouses', views.admin_warehouses_view, name='admin-warehouses'),
    path('admin-add-warehouse', views.admin_add_warehouse_view, name='admin-add-warehouse'),
    path('delete-warehouse/<int:pk>', views.delete_warehouse_view, name='delete-warehouse'),
    path('update-warehouse/<int:pk>', views.update_warehouse_view, name='update-warehouse'),

    path('admin-workers', views.admin_workers_view, name='admin-workers'),
    path('admin-add-worker', views.admin_add_worker_view, name='admin-add-worker'),
    path('delete-worker/<int:pk>', views.delete_worker_view, name='delete-worker'),
    path('update-worker/<int:pk>', views.update_worker_view, name='update-worker'),

    path('admin-work-performed', views.admin_work_performed_view, name='admin-work-performed'),
    path('admin-add-work-performed', views.admin_add_work_performed_view, name='admin-add-work-performed'),
    path('delete-work-performed/<int:pk>', views.delete_work_performed_view, name='delete-work-performed'),
    path('update-work-performed/<int:pk>', views.update_work_performed_view, name='update-work-performed'),

    path('admin-expense', views.admin_expenses_view, name='admin-expense'),
    path('admin-calculation', views.admin_calculation_view, name='admin-calculation'),
    path('update-calculation/<int:pk>', views.update_calculation_view, name='update-calculation'),


    path('admin-uom', views.admin_uom_view, name='admin-uom'),
    path('admin-add-uom', views.admin_add_uom_view, name='admin-add-uom'),
    path('delete-uom/<int:pk>', views.delete_uom_view, name='delete-uom'),
    path('update-uom/<int:pk>', views.update_uom_view, name='update-uom'),

    path('admin-add-material/<int:pk>', views.admin_add_material_view, name='admin-add-material'),
    path('delete-material/<int:pk>', views.delete_material_view, name='delete-material'),
]
