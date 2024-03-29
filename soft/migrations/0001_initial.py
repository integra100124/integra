# Generated by Django 4.2.2 on 2024-01-24 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datea', models.DateTimeField(auto_now_add=True, verbose_name='datea')),
                ('title', models.CharField(max_length=255, verbose_name='application_title')),
                ('details', models.TextField(verbose_name='application_details')),
            ],
            options={
                'db_table': 'application',
                'ordering': ['datea'],
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, verbose_name='catalog_code')),
                ('title', models.CharField(max_length=255, verbose_name='catalog_title')),
                ('details', models.TextField(blank=True, null=True, verbose_name='catalog_details')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='catalog_price')),
            ],
            options={
                'db_table': 'catalog',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='category_title')),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='client_name')),
                ('phone', models.CharField(max_length=32, verbose_name='client_phone')),
                ('leader', models.CharField(max_length=128, verbose_name='client_leader')),
            ],
            options={
                'db_table': 'client',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name='full_name')),
                ('phone', models.CharField(max_length=64, verbose_name='phone')),
            ],
            options={
                'db_table': 'employee',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='position_title')),
            ],
            options={
                'db_table': 'position',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateTimeField(verbose_name='dates')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_catalog', to='soft.catalog')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_client', to='soft.client')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_employee', to='soft.employee')),
            ],
            options={
                'db_table': 'sale',
                'ordering': ['dates'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daten', models.DateTimeField(verbose_name='daten')),
                ('title', models.CharField(max_length=256, verbose_name='news_title')),
                ('details', models.TextField(verbose_name='news_details')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='news_photo')),
            ],
            options={
                'db_table': 'news',
                'ordering': ['daten'],
                'indexes': [models.Index(fields=['daten'], name='news_daten_a29edb_idx')],
            },
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datem', models.DateTimeField(verbose_name='datem')),
                ('status', models.CharField(max_length=128, verbose_name='movement_status')),
                ('details', models.TextField(blank=True, null=True, verbose_name='movement_details')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movement_application', to='soft.application')),
            ],
            options={
                'db_table': 'movement',
                'ordering': ['datem'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_position', to='soft.position'),
        ),
        migrations.AddIndex(
            model_name='client',
            index=models.Index(fields=['name'], name='client_name_57da18_idx'),
        ),
        migrations.AddField(
            model_name='catalog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalog_category', to='soft.category'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['catalog'], name='sale_catalog_6f4233_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['client'], name='sale_client__e86a46_idx'),
        ),
        migrations.AddIndex(
            model_name='sale',
            index=models.Index(fields=['employee'], name='sale_employe_e0273f_idx'),
        ),
        migrations.AddIndex(
            model_name='movement',
            index=models.Index(fields=['application'], name='movement_applica_27871b_idx'),
        ),
        migrations.AddIndex(
            model_name='movement',
            index=models.Index(fields=['datem'], name='movement_datem_8708fe_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['full_name'], name='employee_full_na_b33199_idx'),
        ),
        migrations.AddIndex(
            model_name='employee',
            index=models.Index(fields=['position'], name='employee_positio_c649b1_idx'),
        ),
        migrations.AddIndex(
            model_name='catalog',
            index=models.Index(fields=['title'], name='catalog_title_a1bae3_idx'),
        ),
        migrations.AddIndex(
            model_name='application',
            index=models.Index(fields=['datea'], name='application_datea_198fe9_idx'),
        ),
        migrations.AddIndex(
            model_name='application',
            index=models.Index(fields=['user'], name='application_user_id_ba75f5_idx'),
        ),
    ]
