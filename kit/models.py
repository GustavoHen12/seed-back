from django.db import models
from products.models import Product

#TODO: Adicionar endereço
class Project(models.Model):
    name = models.CharField(
        "Name of the project",
        max_length=60,
    )
    bio = models.CharField(
        "Project Bio",
        max_length=200,
    )
    def __str__(self):
        return self.name

class Kit(models.Model):
    name = models.CharField(
        "Kit name",
        max_length=60,
    )
    description = models.CharField(
        "Kit name",
        max_length=200,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        verbose_name="Name of the project",
        default='',
        null=True,
        blank=True,
    )
    goal = models.IntegerField(
        "Goal number of kits",
    )
    img = models.ImageField(
        default="defaultImage.jpg"
    )
    def __str__(self):
        return self.name

# TODO: Como prevenir que um kit possua produtos repetidos ?
class Kit_product(models.Model):
    kit = models.ForeignKey(
        Kit, 
        on_delete=models.CASCADE,
        verbose_name="Kit",
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,
        verbose_name="Product",
    )
    donated = models.IntegerField(
        "Number of this product donated",
    )

    def __str__(self):
        return self.kit.name