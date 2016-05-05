from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from taggit.managers import TaggableManager


class Topic(models.Model):
    """Notebook topic database table attribute defitions."""
    NOTEBOOK_TYPE = (
        ('M', 'Module'),
        ('E', 'Example'),
    )
    nb_type = models.CharField(
        verbose_name='notebook type',
        default='M',
        max_length=1,
        choices=NOTEBOOK_TYPE,
    )
    name = models.CharField(
        verbose_name='topic name',
        max_length=50,
        help_text='Name of topic.',
    )
    index = models.IntegerField(
        default=0,
        help_text='Index of topic in topic list. Zero indexing.',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['nb_type', 'index', ]


class Notebook(models.Model):
    """Notebook database table attribute defitions."""
    topic = models.ForeignKey(Topic)
    index = models.IntegerField(
        default=0,
        help_text='Index of notebook in notebook list. Zero indexing.',
    )
    published = models.BooleanField(
        # Default is published
        default=1,
        help_text='Untick to not display notebook on page.',
    )
    name = models.CharField(
        max_length=200,
        help_text='Name of notebook.',
    )
    pub_date = models.DateTimeField(
        verbose_name='date published',
        # Not shown in notebook admin page since auto_now_add
        auto_now_add=True,
        null=True,
    )
    edit_date = models.DateTimeField(
        # Not shown in notebook admin page since auto_now
        verbose_name='date edited',
        auto_now=True,
        null=True,
    )
    body = models.TextField(
        verbose_name='explanation',
        max_length=400,
        help_text='A short explanation of the notebook, max length of \
        400 signs including white spaces.',
    )
    file_ipynb = models.FileField(
        # Upload to media server
        verbose_name='.ipynb file',
        upload_to='notebooks',
        null=True,
        help_text='Rendered using Jupyter\'s nbviewer.',
    )
    # From third party app 'django-taggit'
    # Docs: https://django-taggit.readthedocs.org/en/latest/index.html
    tags = TaggableManager(blank=True, )

    def clean(self):
        """Catch unwanted uploads and raise validation errors."""

        # File validation
        file_str = str(self.file_ipynb)
        if file_str[-5:] != 'ipynb':
            raise ValidationError(_('File error. You must upload the \
                notebook in the IPython Notebook format .ipynb.'))

    def __str__(self):
        """Identify notebook by name."""
        return self.name

    class Meta:
        ordering = ['topic__nb_type', 'topic__index', 'index']


class NotebookImage(models.Model):
    """Store media files used in notebooks on server."""
    notebook = models.ForeignKey(
        Notebook,
        related_name='images',
    )
    image = models.ImageField(
        blank=True,
        upload_to='notebooks/images',
        help_text='Images in notebooks has to be included as \
        \'images/file_name\'.',
    )

    def __str__(self):
        return self.image.name
