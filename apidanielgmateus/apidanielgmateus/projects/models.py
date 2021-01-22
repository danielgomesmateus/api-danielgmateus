from django.db import models

from froala_editor.fields import FroalaField


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome:', max_length=35)
    slug = models.SlugField('Identificador:', max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, null=True, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField('Nome:', max_length=50)
    description_short = models.CharField('Descrição curta:', max_length=50)
    content = FroalaField('Conteúdo:')
    cover_image = models.ImageField('Imagem de capa:', max_length=255, upload_to='projects/images')
    slug = models.SlugField('Identificador:', max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-id']

    def __str__(self):
        return self.name


class File(models.Model):
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, null=True, related_name='files', on_delete=models.CASCADE)
    name = models.CharField('Nome:', max_length=50)
    version = models.CharField('Versão:', max_length=50)
    content = FroalaField('Descrição:')
    files = models.FileField('Arquivos do projeto:', max_length=255, upload_to='projects/files')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Download(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome completo:', max_length=50)
    email = models.EmailField('Email de contato:', max_length=40)    
    file = models.ForeignKey(File, related_name='download', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Registro de download'
        verbose_name_plural = 'Registro de download'
        ordering = ['-id']

        def __str__(self):
            return '{} - {}'.format(self.name, self.file)
