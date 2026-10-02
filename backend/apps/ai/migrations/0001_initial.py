from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='PromptTemplate', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=120, unique=True)),('description', models.TextField(blank=True)),('active_version', models.PositiveIntegerField(default=1)),('created_at', models.DateTimeField(auto_now_add=True)),('updated_at', models.DateTimeField(auto_now=True))]),
        migrations.CreateModel(name='AIRequest', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('prompt_name', models.CharField(max_length=120)),('prompt_version', models.CharField(default='1.0.0', max_length=40)),('model', models.CharField(max_length=120)),('latency_ms', models.PositiveIntegerField(default=0)),('prompt_tokens', models.PositiveIntegerField(default=0)),('completion_tokens', models.PositiveIntegerField(default=0)),('total_tokens', models.PositiveIntegerField(default=0)),('estimated_cost_usd', models.DecimalField(decimal_places=8, default=0, max_digits=12)),('status', models.CharField(default='success', max_length=20)),('metadata', models.JSONField(default=dict)),('created_at', models.DateTimeField(auto_now_add=True)),('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name='PromptVersion', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('version', models.PositiveIntegerField()),('system_prompt', models.TextField()),('user_template', models.TextField()),('model', models.CharField(default='gpt-4.1-mini', max_length=120)),('temperature', models.FloatField(default=0.2)),('created_at', models.DateTimeField(auto_now_add=True)),('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='ai.prompttemplate'))]),
    ]
