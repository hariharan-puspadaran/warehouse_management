from django.urls import path
from . import views  #importing from current folder

urlpatterns = [
    path("main/", views.index, name = "main_page-index"),
    path("main/in", views.staff_inbound, name = "staff_inbound"),
    path("main/out", views.staff_outbound, name = "staff_outbound"),
    path("main/inv", views.staff_inventory, name = "staff_inventory"),
    path("main/inbound", views.index_inbound, name = "main_page-inbound"),
    path("main/outbound", views.index_outbound, name = "main_page-outbound"),
    path("main/product", views.index_product, name = "main_page-product"),
    path("staff/",views.staff, name ="main_page-staff"),
    path("staff/detail/<int:pk>",views.staff_detail, name ="main_page-staff-detail"),
    path("inventory/", views.inventory, name = "main_page-inventory"),
    path("inventory/delete/<int:pk>/", views.product_delete, name = "main_page-delete"),
    path("inventory/update/<int:pk>/", views.product_update, name = "main_page-update"),
    path("order/",views.order, name ="main_page-order"),
    path("search/",views.search, name ="search-results"),
    
]


