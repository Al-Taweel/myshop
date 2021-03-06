from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    main_category = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Size(models.Model):
    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    uk_size = models.CharField(max_length=4)

    def __str__(self):
        return self.uk_size

