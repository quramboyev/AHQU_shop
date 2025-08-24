from django.db import models
from parler.models import TranslatableModel, TranslatedFields

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        blank=True,
        null=True,
        verbose_name='Parent Category'
    )
    has_gender = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def get_full_path(self):
        # Возвращает полный путь категории, например: Обувь / Мужская / Кроссовки
        names = []
        category = self
        while category is not None:
            names.append(category.safe_translation_getter('name', any_language=True))
            category = category.parent
        return " / ".join(reversed(names))

    def get_children(self):
        # Возвращает список подкатегорий
        return self.children.all()

    def is_root(self):
        return self.parent is None
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class ColorModel(models.Model):
    name = models.CharField(max_length=30)
    hex_code = models.CharField(max_length=7, blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products')
    created_by_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
        ('unisex', 'Универсальный'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

    class Meta:
        ordering = ['-created_at'] 
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name} - {self.price} сум"

    def formatted_price(self):
        return f"{self.price:,} сум"
    
class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"Фото для{self.product.name}"

