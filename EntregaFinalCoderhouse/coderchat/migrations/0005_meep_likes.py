

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coderchat', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
