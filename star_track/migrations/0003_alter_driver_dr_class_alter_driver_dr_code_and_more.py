# Generated by Django 4.2.1 on 2023-05-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_track', '0002_alter_consignment_cn_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='dr_class',
            field=models.CharField(blank=True, choices=[('1', 'Class 1'), ('2', 'Class 2'), ('3', 'Class 3'), ('4', 'Class 4')], help_text='Class of vehicle driver licensed to drive', max_length=1, null=True, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_code',
            field=models.CharField(blank=True, help_text='A number/code by which driver is identified by', max_length=100, null=True, verbose_name='Assigned Code'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_dob',
            field=models.DateTimeField(blank=True, help_text='Date of birth', null=True, verbose_name='Date Born'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_gender',
            field=models.CharField(choices=[('1', 'Male'), ('2', 'Female')], help_text='Gender of driver', max_length=1, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_licence_date',
            field=models.DateTimeField(blank=True, help_text='Date drver obtained license', null=True, verbose_name='Licensed Date'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_licence_no',
            field=models.CharField(blank=True, help_text='Driver s licence number', max_length=100, null=True, verbose_name='Licence No'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='dr_start_date',
            field=models.DateTimeField(blank=True, help_text='Date joined', null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vh_make',
            field=models.CharField(blank=True, help_text='Make of vehicle', max_length=100, null=True, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vh_model',
            field=models.CharField(blank=True, help_text='Vehicle Model', max_length=100, null=True, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vh_reg_num',
            field=models.CharField(blank=True, help_text='Vehicle s registration number', max_length=100, null=True, verbose_name='Reg. No'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vh_type',
            field=models.CharField(choices=[('1', 'Horse'), ('2', 'Truck'), ('3', 'Standard')], help_text='Vehicle type', max_length=1, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vn_phone_1',
            field=models.IntegerField(blank=True, help_text='Contact person phone number', null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vn_phone_2',
            field=models.IntegerField(blank=True, help_text='Contact person phone number', null=True, verbose_name='Phone'),
        ),
    ]