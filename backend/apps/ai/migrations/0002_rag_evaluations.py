from django.db import migrations, models
import django.db.models.deletion
from pgvector.django import VectorExtension, VectorField

class Migration(migrations.Migration):
    dependencies = [('ai', '0001_initial'), ('core', '0001_initial')]
    operations = [
        migrations.RunSQL('CREATE EXTENSION IF NOT EXISTS vector', reverse_sql=''),
        migrations.CreateModel(name='KnowledgeDocument', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=240)),('content', models.TextField()),('indexed', models.BooleanField(default=False)),('created_at', models.DateTimeField(auto_now_add=True)),('updated_at', models.DateTimeField(auto_now=True)),('workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='knowledge_documents', to='core.workspace'))]),
        migrations.CreateModel(name='DocumentChunk', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('position', models.PositiveIntegerField()),('content', models.TextField()),('embedding', VectorField(dimensions=1536)),('created_at', models.DateTimeField(auto_now_add=True)),('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chunks', to='ai.knowledgedocument'))]),
        migrations.AddConstraint(model_name='documentchunk', constraint=models.UniqueConstraint(fields=('document','position'), name='uniq_document_chunk')),
        migrations.CreateModel(name='EvaluationCase', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('name', models.CharField(max_length=160)),('prompt_name', models.CharField(max_length=120)),('input_variables', models.JSONField(default=dict)),('expected_criteria', models.JSONField(default=list)),('created_at', models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='EvaluationRun', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),('prompt_version', models.CharField(max_length=40)),('score', models.DecimalField(decimal_places=3, default=0, max_digits=6)),('feedback', models.TextField(blank=True)),('passed', models.BooleanField(default=False)),('created_at', models.DateTimeField(auto_now_add=True)),('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='ai.evaluationcase')),('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'))]),
    ]
