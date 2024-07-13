from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Наименование категории",
                            help_text="Введите наименование категории товара"
                            )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание категории",
        help_text="Введите описание категории товара",
    )

    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("name",)


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
    )
    description = models.CharField(
        max_length=255, verbose_name="Описание", help_text="Введите описание товара"
    )
    preview = models.ImageField(
        upload_to="preview/",
        verbose_name="Изображение",
        **NULLABLE,
        help_text="Добавьте изображение товара",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        **NULLABLE,
        related_name="products"
    )
    price = models.FloatField(
        verbose_name="Цена", help_text="Введите стоимость товара"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    in_stock = models.BooleanField(default=True)
    owner = models.ForeignKey(User,
                              verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
                              )

    def __str__(self):
        return f"{self.name} {self.description} {self.category} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("name",)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Продукт",
                                help_text="Название продукта")
    number_version = models.PositiveIntegerField(verbose_name="Номер версии", help_text="Укажите номер версии")
    name = models.CharField(max_length=100, verbose_name="Название версии", help_text="Укажите название версии")
    current_version = models.BooleanField(verbose_name="Признак текущей версии")

    def __str__(self):
        return f"{self.number_version} - {self.name}:{self.current_version}"

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ("number_version", "name")
