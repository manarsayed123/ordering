from django.db import models, IntegrityError
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Sum, F

from order.models import Order
from product.models import Product


class ShopCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_cart_related')

    def add_to_cart(self, product, quantity):
        try:
            self.items.update_or_create(product=product,
                                        defaults={"product": product, "quantity": quantity})
        except IntegrityError:
            pass

        return self

    def delete_from_cart(self, product_id):
        self.items.filter(product_id=product_id).delete()
        return self

    def to_order(self, order):
        total_order_price = self.items.aggregate(sum=Sum(F('product__price') * F('quantity')))['sum']
        self.items.update(order=order, shop_cart=None)
        order.total_price = total_order_price
        order.save()
        return self


class ShopCartItem(models.Model):
    shop_cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE, related_name='items', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='products')
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, null=True, blank=True, related_name="order_items", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        unique_together = ['product', 'shop_cart']


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(signal=post_save, sender='auth.User')
def User_post_save(sender, instance, created, **kwargs):
    """ post signal to create shopcart to user"""
    if created:
        ShopCart.objects.create(user=instance)
