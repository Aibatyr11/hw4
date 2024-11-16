from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True)

    class Meta:
        verbose_name_plural = "Rubrics"
        verbose_name = "Rubric"
        ordering = ['name']

    def __str__(self):
        return self.name


# Create your models here.
class Bb(models.Model):
    rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ('-published',)

    def __str__(self):
        return self.title
