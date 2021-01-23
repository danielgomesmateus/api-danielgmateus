from django.db import models


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título:', max_length=100)
    company = models.CharField('Empresa:', max_length=100)
    description = models.TextField('Descricao:')
    image = models.ImageField('Imagem da empresa:', max_length=255, upload_to='experiences/images')
    started_at = models.DateField('Entrada em:')
    ended_at = models.DateField('Saída em:')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Experiência'
        verbose_name_plural = 'Experiências'
        ordering = ['-id']

    def __str__(self):
        return self.title
