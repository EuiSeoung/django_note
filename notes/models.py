from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    is_html = models.BooleanField(default=False, verbose_name="HTML 코드 적용")

    def __str__(self):
        return self.title