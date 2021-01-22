from django.db import models


class Skill(models.Model):
    RATING_CHOICES = (
        ('1', 'Básico'),
        ('2', 'Iniciante'),
        ('3', 'Bom'),
        ('4', 'Intermediário'),
        ('5', 'Avançado')
    )

    id = models.AutoField(primary_key=True)
    name = models.CharField('Título:', max_length=100)
    rating = models.CharField(max_length=200, choices=RATING_CHOICES)
    image = models.ImageField('Imagem da habilidade:', max_length=255, upload_to='skills/images')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['-id']

    def __str__(self):
        return self.title
