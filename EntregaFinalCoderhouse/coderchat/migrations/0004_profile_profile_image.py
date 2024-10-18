

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderchat', '0003_meep'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
