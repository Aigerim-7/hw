# Generated by Django 4.0.1 on 2022-01-23 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_bookcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertRecomendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recom_text', models.TextField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_recomendation', to='book.book')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('activity', models.CharField(choices=[('BUSINESSMAN', 'BUSINESSMAN'), ('BLOGGER', 'BLOGGER'), ('HOLLYWOOD STAR', 'HOLLYWOOD STAR'), ('DRIVER', 'DRIVER'), ('KILLER', 'KILLER')], max_length=100)),
                ('info', models.TextField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert', to='book.book')),
            ],
        ),
    ]
