from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Notebook(models.Model):
    NOTEBOOK_TYPE = (
        ('M', 'Module'),
        ('E', 'Example')
    )
    MODULE_TOPIC = (
        ('1', 'Basics'),
        ('2', 'Numerical Integration'),
        ('3', 'Root Finding'),
        ('4', 'Ordinary Differential Equations'),
        ('5', 'Linear Algebra'),
        ('6', 'Partial Differential Equations'),
        ('7', 'Python Packages'),
    )
    EXAMPLE_TOPIC = (
        ('1', 'Classical Mechanics'),
        ('2', 'Waves and Acoustics'),
        ('3', 'Thermodynamics'),
        ('4', 'Statistical Mechanics'),
        ('5', 'Electromagnetism'),
        ('6', 'Electronic Circuits'),
        ('7', 'Optics'),
        ('8', 'Quantum Mechanics'),
        ('9', 'Relativity'),
    )
    nb_type = models.CharField(
        verbose_name='notebook type',
        default='M',
        max_length=1,
        choices=NOTEBOOK_TYPE,
    )
    mo_topic = models.CharField(
        verbose_name='module topic',
        max_length=1,
        choices=MODULE_TOPIC,
        # Make it possible to have no module topic
        blank=True,
        help_text='Modules are listed by topic. If you cannot find a \
        topic that fits the content of your module, please contact one \
        of our developers.',
    )
    ex_topic = models.CharField(
        verbose_name='example topic',
        max_length=1,
        choices=EXAMPLE_TOPIC,
        # Make it possible to have no example topic
        blank=True,
        help_text='Examples are listed by topic. If you cannot find a \
        topic that fits the content of your example, please contact one \
        of our developers.',
    )
    published = models.BooleanField(
        # Default is published
        default=1,
        help_text='Tick this box if the notebook should be available to \
        users. Can be useful to not make it available before you have \
        seen to that everything is in order.',
    )
    title = models.CharField(
        max_length=200,
        help_text='Notebooks are listed by topic and increasing numbers \
        under each topic. You have to add the number the notebooks \
        topic has in the topic list and the notebook number at the \
        start of the title. E.g. \'11 Lennard-Jones Potential\', if it \
        were the first notebook in the \'Classical Mechanics\' topic.',
    )
    slug = models.SlugField(
        # Automatically filled from filling in title
        verbose_name='url',
        help_text='Url of notebook, e.g. \'numfys.net/modules/url\'.',
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
        help_text='NB! We have a file naming convention: \
        \'mo_b1_basic_plotting.ipynb\' for the notebook  Basic \
        Plotting, Module 1, Basics topic, e.g. Rendered using \
        Jupyter\'s nbviewer.',
    )

    class Meta:
        ordering = ['nb_type', 'title']

    def clean(self):
        """Catch unwanted uploads and raise validation errors."""

        # Type validation
        if self.nb_type == 'M' and self.ex_topic != '' \
                or self.nb_type == 'E' and self.mo_topic != '':
            raise ValidationError(_('Notebook type error. Notebook type \
                and choice of topic doesn\'t match.'))

        # Title validation
        if self.title[:2].isdigit() is False:
            raise ValidationError(_('Title error. Notebook title must \
            start with topic number and notebook entry in the topic, \
            e.g. \'11 Lennard-Jones Potential \'. This is so that the \
            notebooks are easy to sort and the title will be displayed \
            correctly.'))

        # Topic validation
        if self.mo_topic == '' and self.ex_topic == '':
            raise ValidationError(_('Topic error. Notebook must have a \
                topic.'))
        if self.mo_topic != '' and self.ex_topic != '':
            raise ValidationError(_('Topic error. Notebook cannot have \
                both a module topic and an example topic.'))
        if self.mo_topic:
            if self.title[:2].isdigit() and self.title[0] != self.mo_topic:
                raise ValidationError(_('Title error. Notebook title \
                    and topic number doesn\'t match. E.g. \'11 \
                    Lennard-Jones Potential\' corresponds to topic 1, \
                    \'Classical Mechanics\', in the example topic \
                    list.'))
        else:
            if self.title[:2].isdigit() and self.title[0] != self.ex_topic:
                raise ValidationError(_('Title error. Notebook title \
                    and topic number doesn\'t match. E.g. \'11 \
                    Lennard-Jones Potential\' corresponds to topic 1, \
                    \'Classical Mechanics\', in the example topic \
                    list.'))

        # File validation
        file_str = str(self.file_ipynb)
        if file_str[-5:] != 'ipynb':
            raise ValidationError(_('File error. You must upload the \
                notebook in the IPython Notebook format .ipynb.'))
        if (file_str[0:3] != ('mo_' or 'ex_') and
                file_str[10:13] != ('mo_' or 'ex_')):
            print(file_str[0:3], file_str[10:13])
            raise ValidationError(_('File error. You must follow the \
                naming convention: \'mo_b1_basic_plotting.ipynb\' \
                for the notebook Basic Plotting, Module 1, Basics \
                topic, e.g.'))

    def __str__(self):
        """Identify notebook object by title."""
        return self.title


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
