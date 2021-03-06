from django.urls import path
import shoppingapp.views as shoppingapp


app_name = 'shoppingapp'
urlpatterns = [
    path('', shoppingapp.view_group_purchases, name='shoppinglist'),
    path('purchasecreation/', shoppingapp.purchasecreation_page, name='purchasecreation'),
    path('purchasedetails/<item_pk>/', shoppingapp.purchase_edit, name='purchasedetails'),
    path('purchasedelete/<item_pk>/', shoppingapp.removeitem, name='purchaseremove'),
    path('checkbox/<item_pk>/', shoppingapp.checkbox_shop_list, name='checkbox'),
]