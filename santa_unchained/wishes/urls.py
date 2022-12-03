from django.urls import path

from santa_unchained.wishes.views import (
    WishListSuccessView,
    WishListDetailView,
    WishListFormView
)

app_name = "wishes"

urlpatterns = [
    path("success/<slug:slug>/", WishListSuccessView.as_view(), name="success"),
    path("<slug:slug>/", WishListDetailView.as_view(), name="wishlist-detail"),
    path("", WishListFormView.as_view(), name="wishlist"),
]
