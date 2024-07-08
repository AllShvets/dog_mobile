from django.db import models


class EncyclopediaRecord(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание статьи')
    full_text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(
        upload_to='article_files',
        blank=False,
        verbose_name='Картинка'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительская статья'
    )

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
