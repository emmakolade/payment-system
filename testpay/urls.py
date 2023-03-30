from .views import FundWalletView, WalletBalanceView, PaymentAutomationView, ProductCreateView, ProductListView, PaymentStopView, PaymentListView
from django.urls import path


urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/list/', ProductListView.as_view(), name='product-list'),


    path('wallet/fund/', FundWalletView.as_view(), name='fund-wallet'),
    path('wallet/balance/', WalletBalanceView.as_view(), name='wallet-balance'),


    path('payment-automation/<int:product_id>/',
         PaymentAutomationView.as_view(), name='payment-automation'),
    path('payment/<int:product_id>/stop/',
         PaymentStopView.as_view(), name='payment-stop'),
    path('payment/list/', PaymentListView.as_view(), name='payment_list'),
]
