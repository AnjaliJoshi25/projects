from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subheading', models.CharField(max_length=200, blank=True, null=True)),  # Add subheading field
                ('topics', models.CharField(max_length=100)),  # Add topics field
                ('cont', models.TextField()),
                # ('image', models.ImageField(upload_to='blog/images/', blank=True, null=True)),  # Add image field
            ],
        ),
    ]
