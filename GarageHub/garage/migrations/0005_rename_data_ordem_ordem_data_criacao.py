# Generated by Django 5.0.3 on 2024-04-14 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_ordem_autor_veiculo_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordem',
            old_name='data_ordem',
            new_name='data_criacao',
        ),
    ]
