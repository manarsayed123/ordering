from django.db import models


# Create your models here.
class Product(models.Model):
    DRAFT = "DRAFT"
    PUBLISHED = "PUBLISHED"

    product_status = (
        (DRAFT, DRAFT),
        (PUBLISHED, PUBLISHED)
    )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    status = models.CharField(choices=product_status, max_length=10, default=DRAFT)

    def __str__(self):
        return self.name
