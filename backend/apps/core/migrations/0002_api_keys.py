from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings

class Migration(migrations.Migration):
    dependencies = [('core','0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='APIKey', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=120)),('prefix', models.CharField(max_length=12, unique=True)),('key_hash', models.CharField(max_length=128, unique=True)),('last_used_at', models.DateTimeField(blank=True, null=True)),('revoked_at', models.DateTimeField(blank=True, null=True)),('created_at', models.DateTimeField(auto_now_add=True)),('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_keys', to=settings.AUTH_USER_MODEL))]),
    ]
