from django.db import models

# Create your models here.

class Produto(models.Model):

    situacao = [
        ('n', 'novo'),
        ('u', 'usado'),
        ('r', 'recuperado'),
    ]
    processador = [
        ('core', 'core 2duo'),
        ('i3', 'core i3'),
        ('i5', 'core i5'),
        ('i7', 'core i7'),
        ('i9', 'core i9'),
    ]
    memoria = [
        ('256', 'DDR3 256MB'),
        ('512', 'DDR3 512MB'),
        ('1GB', 'DDR3 1GB'),
        ('2GB', 'DDR3 2GB'),
        ('4GB', 'DDR3 4GB'),
        ('8GB', 'DDR3 8GB'),
        ('16GB', 'DDR3 16GB'),
    ]
    hd = [
        ('128', '128 gb'),
        ('320', '320 gb'),
        ('500', '500 gb'),
        ('1', '1 tb'),
        ('2', '2 tb'),
    ]


    nome = models.CharField('Nome', max_length=45)
    marca = models.CharField('Marca', max_length=45)
    estado = models.CharField('Estado', max_length=10, choices=situacao)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    tela = models.DecimalField('Tela', max_digits=8, decimal_places=2)
    pro_cessador = models.CharField('Processador', max_length=10, choices=processador)
    m_ram = models.CharField('Memoria Ram', max_length=10, choices=memoria)
    storage = models.CharField('Armazenamento', max_length=10, choices=hd)
    estoque = models.IntegerField('Estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    #criação de um choice, escolha a ser feita sobre um tipo
    status = (

        ('M', 'masculino'),
        ('F', 'feminino'),
    )

    nome = models.CharField('Nome', max_length=50,)
    sobrenome = models.CharField('Sobre nome', max_length=30)
    sexo = models.CharField('Sexo', max_length=1, choices=status)
    email = models.EmailField('E-mail', max_length=80)

    def __str__(self):
        return self.nome