from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок', help_text='Введите заголовок статьи')
    slug = models.CharField(max_length=100, verbose_name='slug', help_text='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержание', help_text='Введите текст статьи')
    preview = models.ImageField(upload_to='preview/', verbose_name='Превью', help_text='Загрузить превью статьи',
                                **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    published = models.BooleanField(default=True, verbose_name='Признак публикации',
                                    help_text='Укажите признак публикации статьи')
    number_views = models.PositiveIntegerField(verbose_name='Количество просмотров',
                                               help_text='Укажите количество просмотров статьи', default=0)

    def __str__(self):
        return f'{self.title} {self.slug} {self.content}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('title',)
        permissions = [("can_manage_publications", "can manage publications")]
