from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [('core','0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(name='ContentDocument', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('title', models.CharField(max_length=240)),('content', models.TextField(blank=True)),('content_type', models.CharField(default='blog', max_length=40)),('tone', models.CharField(default='professional', max_length=40)),('metadata', models.JSONField(default=dict)),('version', models.PositiveIntegerField(default=1)),('created_at', models.DateTimeField(auto_now_add=True)),('updated_at', models.DateTimeField(auto_now=True)),('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='core.workspace'))]),
        migrations.CreateModel(name='ContentVersion', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('version', models.PositiveIntegerField()),('content', models.TextField()),('prompt_snapshot', models.JSONField(default=dict)),('created_at', models.DateTimeField(auto_now_add=True)),('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='content.contentdocument'))]),
        migrations.AlterUniqueTogether(name='contentversion', unique_together={('document','version')}),
    ]
