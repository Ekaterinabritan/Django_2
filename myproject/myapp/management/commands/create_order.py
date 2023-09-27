from random import choices
from django.core.management.base import BaseCommand
from myproject.myapp.models import User, Product, Order

class Command(BaseCommand):
    help = "Create order"
class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument("User_id", type=int, help="User ID")
        parser.add_argument('-p', '--Product_id', nargs='+', help="User ID", required=True)

    def handle(self, *args, **kwargs):
        User_id = kwargs.get('User_id')
        Product_id: list = kwargs.get('Product_id')

        user = User.objects.filter(pk=User_id).first()

        order = Order(customer=user)
        total_price = 0
        for i in range(0, len(Product_id)):
            product = Product.objects.filter(pk=Product_id[i]).first()
            total_price += float(product.price)
            order.total_price = total_price
            order.save()
            order.products.add(product)