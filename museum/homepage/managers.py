from django.db import models

from . import models as local_models


class PostManager(models.Manager):
    def select_main(self):
        return (
            self.get_queryset()
                .all()
                .order_by('created_on')
                .prefetch_related(
                    models.Prefetch(
                        'tags',
                        queryset=local_models.Tag.objects.all()
                    )
                )
        )
