# Generated by Django 4.1.2 on 2022-10-29 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_restaurant_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='picture',
            field=models.ImageField(default='/static/images/dess1.png', upload_to='static/images/'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=250)),
                ('rate', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
