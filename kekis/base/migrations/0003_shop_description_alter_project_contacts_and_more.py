# Generated by Django 4.0.2 on 2023-05-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_shop_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='description',
            field=models.CharField(default='No description yest', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='contacts',
            field=models.ManyToManyField(to='base.Contacts', verbose_name='Кониакты учеников'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='base.Image', verbose_name='Дополнительные изображения'),
        ),
    ]