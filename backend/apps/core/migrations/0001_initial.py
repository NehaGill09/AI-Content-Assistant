from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='Workspace', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=120)),('created_at', models.DateTimeField(auto_now_add=True)),('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workspaces', to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name='AuditEvent', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('action', models.CharField(max_length=120)),('metadata', models.JSONField(default=dict)),('created_at', models.DateTimeField(auto_now_add=True)),('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL))]),
    ]
