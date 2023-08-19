from django.db import models


class Сurrency(models.Model):
    char_code = models.CharField(max_length=3, verbose_name="Код")
    name = models.CharField(max_length=150, verbose_name="Название")

    def __str__(self):
        return self.char_code

    class Meta:
        verbose_name_plural = "Валюты"


class Rate(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата сбора данных")
    value = models.DecimalField(max_digits=7, decimal_places=4, verbose_name="Значение")
    currency = models.ForeignKey(
        Сurrency, related_name="rates", verbose_name="Валюта", on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ["date", "currency"]
        verbose_name_plural = "Курсы валют"
