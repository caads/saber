from django.db import models

class Inscricao (models.Model):
    numeroInscricao = models.AutoField(primary_key=True)
    nome = models.CharField("Nome", max_length=100)
    cpf = models.CharField ("CPF", max_length=11, unique=True)
    telefone = models.CharField ("Telefone", max_length=13)
    email= models.EmailField("Email",max_length=50)
    TAMANHOCAMISA_CHOICES = (
        ('P', 'P'),
        ('M', 'M'),
    	('G', 'G'),
	    ('GG', 'GG'),
	  	('XG', 'XG'),
    )
    tamanhocamisa = models.CharField("Tamanho da Camisa", max_length=2, choices=TAMANHOCAMISA_CHOICES)
    DEFICIENCIA_CHOICES = (
        ('SIM', 'Sim'),
        ('NAO', 'Nao'),
    )
    deficienciaF = models.CharField("Deficiencia Fisica", max_length=3, choices=DEFICIENCIA_CHOICES)
    qual = models.CharField('Qual', max_length=100, blank=True)
    def __unicode__(self):
        return self.nome




    	
