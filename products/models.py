from django.db import models

class Outfitter(models.Model):
    name = models.CharField(
        "Outfitter Name",
        max_length=60,
    )
    quotation_date = models.DateField(
        "Quotation Date",
    )
    website = models.URLField(
        "Website link",
        max_length=200,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        "Product Name",
        max_length=60,
    )
    description = models.CharField(
        "Product Description",
        max_length=140,
    )
    img = models.ImageField(
        default="defaultImage.jpg"
    )
    price = models.DecimalField(
        "Product Price",
        max_digits=10, 
        decimal_places=2,
    )
    in_kit = models.IntegerField(
        "Number of this product in a kit",
    )
    outfitter = models.ForeignKey(
        Outfitter,
        on_delete=models.CASCADE,
        verbose_name="Product outfitter",
        default=-1,
    )
    
    def __str__(self):
        return self.name
