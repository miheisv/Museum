from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all()
    )
    class Meta:
        model = Post
        fields = (
            Post.name.field.name,
            Post.title.field.name,
            Post.description.field.name,
            'main_picture',
            Post.text.field.name,
            Post.tags.field.name,
        )
        labels = {
            Post.name.field.name: 'Название записи',
            Post.title.field.name: 'Заголовок поста',
            Post.description.field.name: 'Описание поста',
            'main_picture': 'Главное изображение',
            Post.text.field.name: 'Основной текст',
            Post.tags.field.name: 'Теги',
        }
        help_texts = {
            Post.name.field.name: 'Выберите название записи',
            Post.title.field.name: 'Выберите заголовок поста',
            Post.description.field.name: 'Введите краткое описание',
            'main_picture': 'Выберите изображение размером ?x?',
            Post.tags.field.name: 'Выберите теги, подходящие вашему посту',
        }


    def save(self, commit=True):
        post = super(PostForm, self).save(commit=True)
        post.save()
        return post


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
