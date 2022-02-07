from django.db import models

class CustomerCL(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class ClothesCL(models.Model):
    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежды'

    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)


    def __str__(self):
        return self.name



class OrderCL(models.Model):
    STATUS = (
        ('Обрабатывается','Обрабатывается'),
        ('Выехал','Выехал'),
        ('Доставлен','Доставлен')
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ClothesCL,
                                on_delete=models.CASCADE,
                                related_name='order_product')
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=STATUS)

    def __str__(self):
        return self.product.name

