from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse
from lxml.html import fromstring
from Core.models import NamedBaseModel
from .managers import PostManager


pattern = '<[^<]+?>'


class Tag(NamedBaseModel):
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        default_related_name = 'tags'


class Post(NamedBaseModel):
    main_picture = models.ImageField(
        'post picture',
        upload_to='images/%Y/%m',
        blank=True,
    )
    title = models.CharField(
        'title',
        max_length=120,
        blank=True,
        help_text='Заголовок поста'
    )
    text = tinymce_models.HTMLField(
        verbose_name='description',
        help_text='Основной текст поста',
        blank=True,
    )
    description = models.TextField(
        verbose_name='Краткое описание',
        max_length=150,
        help_text='Введите краткое описание',
        default='',
    )
    created_on = models.DateTimeField(
        'created on',
        help_text='datetime of post creation',
        auto_now_add=True,
    )
    views = models.PositiveIntegerField(
        'views',
        blank=True,
        default=0,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='tags',
        help_text='Post tags'
    )

    objects = PostManager()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        default_related_name = 'posts'

    def get_absolute_url(self):
        self.views += 1
        self.save()
        return reverse('homepage:post', kwargs={"pk": self.pk})
    
    def get_short_text(self):
        if self.description:
            return self.description
        text = self.text
        parserObj = fromstring(text)
        outputString = str(parserObj.text_content())
        return outputString[:120]

    def __str__(self):
        return f'{self.name}:{self.title}:'
