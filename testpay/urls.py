from .views import PaymentCreateView, PaymentMethodEditView, PaymentHistoryView, PaymentAutomationView
from django.urls import path


urlpatterns = [
    path('payment-create/', PaymentCreateView.as_view(),
         name='payment-create'),
    path('payment-edit/', PaymentMethodEditView.as_view(),
         name='payment-edit'),
    path('payment-history/', PaymentHistoryView.as_view(),
         name='payment-history'),
    path('payment-automate/', PaymentAutomationView.as_view(),
         name='payment-automate'),
]
