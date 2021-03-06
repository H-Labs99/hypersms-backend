# Generated by Django 3.2.5 on 2022-02-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiwassa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sms',
            name='taille',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Taille du sms'),
        ),
        migrations.AlterField(
            model_name='client',
            name='auth_code',
            field=models.IntegerField(blank=True, default=55942, null=True, verbose_name="Code d'authentification"),
        ),
        migrations.AlterField(
            model_name='config',
            name='entete',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='Entete des SMS'),
        ),
        migrations.AlterField(
            model_name='sms',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Texte'),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='nbr_sms_sent',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Nombre de sms envoyé'),
        ),
        migrations.AlterField(
            model_name='souscription',
            name='numero',
            field=models.IntegerField(blank=True, default=714352, null=True),
        ),
    ]
