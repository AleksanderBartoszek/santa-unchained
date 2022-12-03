from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField

class WishListStatuses(models.TextChoices):
    NEW = "NEW", _("New")
    ACCEPTED = "ACCEPTED", _("Accepted")
    REJECTED = "REJECTED", _("Rejected")
    READY_FOR_SHIPPING = "READY_FOR_SHIPPING", _("Ready for shipping")
    DELIVERED = "DELIVERED", _("Delivered")

class Address(models.Model):
    street = models.CharField(max_length = 30)
    post_code = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length = 30)
    lng = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0,
    )
    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        default=0,
    )

class WishList(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    content = models.TextField(max_length=1000)
    status = models.CharField(
        max_length=18, 
        choices=WishListStatuses.choices,
        default=WishListStatuses.NEW
    )
    slug = AutoSlugField(populate_from=['name', 'content', 'address'])
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

class WishListItem(models.Model):
    wish_list = models.ForeignKey(WishList, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    approved = models.BooleanField(default=False)


class NewWishListManager(models.Manager):
    """
    Manager which filters only new wish lists.
    """

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=WishListStatuses.NEW)


class WishListNew(WishList):
    objects = NewWishListManager()

    class Meta:
        proxy = True
        verbose_name = _("new wish list")
        verbose_name_plural = _("new wish lists")


class WishListAccepted(WishList):
    objects = NewWishListManager()

    class Meta:
        proxy = True
        verbose_name = _("accepted wish list")
        verbose_name_plural = _("accepted wish lists")


class WishListRejected(WishList):
    objects = NewWishListManager()

    class Meta:
        proxy = True
        verbose_name = _("rejected wish list")
        verbose_name_plural = _("rejected wish lists")


class WishListReady(WishList):
    objects = NewWishListManager()

    class Meta:
        proxy = True
        verbose_name = _("ready to be sent wish list")
        verbose_name_plural = _("ready to be sent wish lists")


class WishListDelivered(WishList):
    objects = NewWishListManager()

    class Meta:
        proxy = True
        verbose_name = _("delivered wish list")
        verbose_name_plural = _("delivered wish lists")
