# Generated by Django 4.2.2 on 2023-06-24 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colaboradores', '0002_alter_colaborador_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colaborador',
            options={'permissions': (('permissao_gerente', 'permissao gerente'), ('permissao_supervisor', 'permissao supervisor'), ('permissao_vendedor', 'permissao vendedor'), ('permissao_funcionario', 'permissao todos funcionarios')), 'verbose_name_plural': 'Colaboradores'},
        ),
    ]
