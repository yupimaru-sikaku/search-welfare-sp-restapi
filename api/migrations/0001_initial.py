# Generated by Django 3.1 on 2022-02-12 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=50, unique=True)),
                ('companyNumber', models.CharField(max_length=13, unique=True)),
                ('postalCode', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=100)),
                ('telephoneNumber', models.CharField(max_length=11)),
                ('faxNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('humanName', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeName', models.CharField(max_length=50, unique=True)),
                ('postalCode', models.CharField(max_length=7)),
                ('address', models.CharField(max_length=100)),
                ('telephoneNumber', models.CharField(max_length=11)),
                ('faxNumber', models.CharField(blank=True, max_length=11, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('humanName', models.CharField(max_length=10)),
                ('capacity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeNumber', models.CharField(max_length=11, unique=True)),
                ('serviceType', models.CharField(choices=[('共同生活援助（介護サービス包括型）', '共同生活援助（介護サービス包括型）'), ('就労継続支援B型）', '就労継続支援B型'), ('生活介護）', '生活介護'), ('計画相談支援', '計画相談支援'), ('重度訪問介護', '重度訪問介護'), ('児童発達支援', '児童発達支援'), ('障がい児相談支援', '障がい児相談支援'), ('重度訪問介護', '重度訪問介護')], default='共同生活援助（介護サービス包括型）', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.office')),
            ],
        ),
    ]
