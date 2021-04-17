# Generated by Django 3.1.4 on 2021-04-17 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_user_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creator', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to=settings.AUTH_USER_MODEL)),
                ('src_poll', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fork_polls', to='myapp.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('poll', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='poll_questions', to='myapp.poll')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('question', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='question_replies', to='myapp.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ans_type', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, related_name='question_answers', to='myapp.question')),
            ],
        ),
    ]