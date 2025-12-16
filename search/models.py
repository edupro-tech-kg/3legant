from django.db import models

class SearchQueryLog(models.Model):
    query = models.CharField(max_length=255, verbose_name="Поисковый запрос")
    results_count = models.PositiveIntegerField(default=0, verbose_name="Кол-во результатов")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата запроса")

    class Meta:
        verbose_name = "Поисковый запрос"
        verbose_name_plural ="Поисковые запросы"
        ordering = ("-created_at",)
    def __str__(self):
        return f"{self.query}({self.results_count})"