from django.db import models

class Detail(models.Model):
    id_details= models.AutoField(primary_key=True)
    color_details = models.CharField(max_length=50,null=False,blank=False)
    weight_details = models.IntegerField(default=0)
    size_details = models.CharField(max_length=1)
    height_details = models.DecimalField(max_digits=3, decimal_places=2)
    width_details = models.DecimalField(max_digits=3, decimal_places=2)
    depth_details = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.id +'-'+ self.color_details

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

class Seller(models.Model):
    id_seller = models.AutoField(primary_key=True)
    name_seller = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
        
class Product(models.Model):
    id_product = models.BigAutoField(primary_key=True)
    sku_product = models.CharField(max_length=10, null=False, blank=False)
    qr_product = models.CharField(max_length=10, null=False, blank=False)
    name_product = models.CharField(max_length=100, null=False,blank=False)
    price_product = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    descriptions_product = models.CharField(max_length=100, null=True, blank=True)
    brand_product=models.CharField(max_length=50, null=True, blank=True)
    image_product = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    stock_product = models.IntegerField(default=0)
    id_details = models.ForeignKey(Detail, on_delete=models.CASCADE)
    id_seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=100, null=False,blank=False)
    descriptions_category = models.CharField(max_length=100, null=True, blank=True)
    image_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

class Product_Category(models.Model):
    id_product_category = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name +'-'+ self.category.name