from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Example(models.Model):
    TOPIC = (
        ('ME', 'Mechanics'),
        ('WA', 'Waves and Acoustics'),
        ('TD', 'Thermodynamics'),
        ('EC', 'Electronic Circuits'),
        ('OP', 'Optics'),
        ('QM', 'Quantum Mechanics'),
    )
    title = models.CharField(
        max_length=100,
        help_text='Examples are listed by increasing numbers under each \
        topic, hence you have to add a number first in the title like \
        \'1.1 Lennard Jones Potential\'.',
    )
    slug = models.SlugField(
        verbose_name='Web address',
        help_text='URL of example, \'numfys.net/examples/slug\'.',
    )
    pub_date = models.DateTimeField(
        verbose_name='Date published',
        auto_now_add=True,
        null=True,
    )
    edit_date = models.DateTimeField(
        verbose_name='Date edited',
        auto_now=True,
        null=True,
    )
    topic = models.CharField(
        default='ME',
        max_length=3,
        choices=TOPIC,
        help_text='Examples are listed by topic. If you cannot find a \
        topic that fits the content of your module, please contact the \
        developer(s).',
    )
    body = models.TextField(
        help_text='A short explanation of the example.',
    )
    file_html = models.FileField(
        verbose_name='.html file',
        upload_to='files/examples/html',
        null=True,
    )
    file_ipynb = models.FileField(
        verbose_name='.ipynb file',
        upload_to='files/examples/ipynb',
        null=True,
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ExampleImage(models.Model):
    """Add media files used in notebooks to server."""
    example = models.ForeignKey(
        Example,
        related_name='images',
    )
    image = models.ImageField(
        blank=True,
        upload_to='files/examples/img',
        help_text='Images in notebooks has to be included as \
        \'../img/file_name\'.',
    )

    def __str__(self):
        return self.image.name


# For some reason, files are only deleted from the database and not the
# server. The following code makes sure it does.
@receiver(pre_delete, sender=Example)
def example_delete(sender, instance, **kwargs):
    instance.file_html.delete(False)
    instance.file_ipynb.delete(False)


@receiver(pre_delete, sender=ExampleImage)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)
