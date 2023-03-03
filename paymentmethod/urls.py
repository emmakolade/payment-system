from .views import PaymentMethodCreateView, PaymentHistoryListView, RecurringPaymentView
from django.urls import path


urlpatterns = [
    path('payment-methods/', PaymentMethodCreateView.as_view(),
         name='payment-method-create'),
    path('payment-history/', PaymentHistoryListView.as_view(),
         name='payment-history-list'),
    # path('payment/', PaymentView.as_view(),
    #      name='payment'),
    path('recurring/', RecurringPaymentView.as_view(),
         name='recurring'),
]
