from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.forms.widgets import FileInput


class Module(models.Model):
    # Maximum length of topic: 3
    TOPIC = (
        ('BC', 'Basics'),
        ('NI', 'Numerical Integration'),
        ('RF', 'Root Finding'),
        ('ODE', 'Ordinary Differential Equations'),
        ('LA', 'Linear Algebra'),
        ('PDE', 'Partial Differential Equations'),
        ('PP', 'Python Packages'),
    )
    title = models.CharField(
        max_length=100,
        help_text='Modules are listed by increasing numbers under each \
        topic, hence you have to add a number first in the title like \
        \'1.5 Basic Plotting\'.',
    )
    slug = models.SlugField(
        verbose_name='Web adress',
        help_text='URL of module, \'numfys.net/modules/slug\'.')
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
        default='BC',
        max_length=3,
        choices=TOPIC,
        help_text='Modules are listed by topic. If you cannot find a \
        topic that fits the content of your module, please contact the \
        developer(s).',
    )
    body = models.TextField(
        help_text='A short explanation of the module.',
    )
    file_html = models.FileField(
        verbose_name='.html file',
        null=True,
        upload_to='files/modules/html',
    )
    file_ipynb = models.FileField(
        verbose_name='.ipynb file',
        null=True,
        upload_to='files/modules/ipynb',
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class ModuleImage(models.Model):
    """Add media files used in notebooks to server."""
    module = models.ForeignKey(
        Module,
        related_name='images',
    )
    image = models.ImageField(
        blank=True,
        upload_to='files/modules/img',
        help_text='Images in notebooks has to be included as \
        \'../img/file_name\'.',
    )

    def __str__(self):
        return self.image.name


# For some reason, files are only deleted from the database and not the
# server. The following code makes sure it does.
@receiver(pre_delete, sender=Module)
def module_delete(sender, instance, **kwargs):
    instance.file_html.delete(False)
    instance.file_ipynb.delete(False)


@receiver(pre_delete, sender=ModuleImage)
def image_delete(sender, instance, **kwargs):
    instance.image.delete(False)
