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
    # The img field is optional and the imgUrl exist because
    # the heroku server dont keep static photos saved, so the
    # img url is an option
    img = models.ImageField(
        default="defaultImage.jpg",
        null=True,
        blank=True,
    )
    imgUrl = models.URLField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        "Product Price",
        max_digits=10, 
        decimal_places=2,
    )
    outfitter = models.ForeignKey(
        Outfitter,
        on_delete=models.CASCADE,
        verbose_name="Product outfitter",
        default=-1,
    )
    
    def __str__(self):
        return self.name
