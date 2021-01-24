from django.db import models


class AcademicFormation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nome:', max_length=100)
    institution = models.CharField('Instituição:', max_length=100)
    started_at = models.DateField('Entrada em:')
    ended_at = models.DateField('Saída em:', blank=True, null=True)
    image = models.ImageField('Imagem da instituição:', max_length=255, upload_to='academic_formations/images')
    status = models.BooleanField('Status:', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Formação acadêmica'
        verbose_name_plural = 'Formações acadêmica'
        ordering = ['-id']

    def __str__(self):
        return self.name
