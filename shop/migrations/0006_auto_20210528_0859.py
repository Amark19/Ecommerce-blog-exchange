# Generated by Django 3.0.7 on 2021-05-28 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_sellerdetails_img2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerdetails',
            name='location',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='bookauthor',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='bookcategory',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='bookname',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='latt',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='longi',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sellerdetails',
            name='usedtime',
            field=models.CharField(max_length=50),
        ),
    ]