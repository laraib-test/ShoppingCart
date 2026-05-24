from django.core.management.base import BaseCommand

from shoppinglist.models import (
    Category,
    Store,
    Product,
    Price
)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        products = [

            ("Milk", "Dairy", 4.99, "Walmart", 2.5, "L"),
            ("Milk", "Dairy", 6.99, "FreshCo", 2.0, "L"),

            ("Eggs", "Dairy", 2.99, "Walmart", 12, "pcs"),
            ("Eggs", "Dairy", 3.49, "FreshCo", 12, "pcs"),

            ("Block Cheese", "Dairy", 5.99, "Walmart", 500, "g"),
            ("Block Cheese", "Dairy", 7.99, "FreshCo", 500, "g"),

            ("Glee Butter", "Dairy", 3.99, "Walmart", 250, "g"),
            ("Glee Butter", "Dairy", 4.99, "FreshCo", 250, "g"),

            ("Bananas", "Fruits", 0.99, "Walmart", 6, "pcs"),
            ("Bananas", "Fruits", 2.49, "FreshCo", 6, "pcs"),

            ("Apples", "Fruits", 3.49, "FreshCo", 6, "pcs"),
            ("Apples", "Fruits", 2.99, "Walmart", 6, "pcs"),

            ("Oranges", "Fruits", 2.49, "Walmart", 6, "pcs"),
            ("Oranges", "Fruits", 2.99, "FreshCo", 6, "pcs"),

            ("Carrots", "Vegetables", 2.99, "Walmart", 1, "pcs"),
            ("Carrots", "Vegetables", 3.49, "FreshCo", 1, "pcs"),

            ("Broccoli", "Vegetables", 2.49, "Walmart", 1, "pcs"),
            ("Broccoli", "Vegetables", 3.99, "FreshCo", 1, "pcs"),

            ("Chicken Breast", "Meat", 12.99, "Walmart", 250, "g"),
            ("Chicken Breast", "Meat", 14.99, "FreshCo", 250, "g"),

            ("Ground Beef", "Meat", 10.99, "FreshCo", 500, "g"),
            ("Ground Beef", "Meat", 9.99, "Walmart", 500, "g"),
        ]

        for name, category_name, price_value, store_name, quantity, unit in products:

            # Category
            category, _ = Category.objects.get_or_create(
                name=category_name
            )

            # Store
            store_locations = {
            "Walmart": "Calgary NE",
            "FreshCo": "Downtown Calgary",
             }
            store, created = Store.objects.get_or_create(
              name=store_name
            )

            store.location = store_locations.get(store_name)
            store.save()

            # Product
            product, created = Product.objects.get_or_create(
                name=name,
                category=category,
                defaults={
                    "quantity": quantity,
                    "unit": unit,
                }
            )

            # Update quantity/unit if already exists
            if not created:

                product.quantity = quantity
                product.unit = unit
                product.save()

            # Price
            Price.objects.update_or_create(
                product=product,
                store=store,
                defaults={
                    "price": price_value
                }
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Seed data inserted successfully."
            )
        )