# Generated by Django 2.2 on 2019-06-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busapp', '0003_auto_20190617_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elite',
            name='User',
        ),
        migrations.AlterField(
            model_name='elite',
            name='Bus_number',
            field=models.CharField(choices=[('VJ6531-LB', 'VJ6531-LB'), ('VJ6532-UB', 'VJ6532-UB'), ('VJ6533-LB', 'VJ6523-LB'), ('VJ6534-UB', 'VJ6524-UB'), ('GT4505', 'GT4505'), ('GT4506', 'GT4506'), ('GT4507', 'GT4507'), ('WG6628-UB', 'WG6628-UB'), ('WG6629-LB', 'WG6629-LB'), ('HY4555', 'HY4555'), ('HY4556', 'HY4556'), ('HY4557', 'HY4557'), ('HY4558', 'HY4558'), ('HY4559', 'HY4559'), ('HY4560', 'HY4560'), ('HY4561', 'HY4561'), ('WG6630-UB', 'WG6630-UB'), ('WG6631-LB', 'WG6631-LB'), ('WG6632-UB', 'WG6632-UB'), ('WG6633-LB', 'WG6633-LB'), ('WG6634-UB', 'WG6634-UB'), ('GT4508', 'GT4508'), ('GT4509', 'GT4509'), ('GT4510', 'GT4510'), ('GT4511', 'GT4511'), ('VJ6535-LB', 'VJ6525-LB'), ('VJ6536-UB', 'VJ6526-UB'), ('VJ6537-LB', 'VJ6527-LB'), ('VJ6538-UB', 'VJ6528-UB'), ('VJ6539-LB', 'VJ6529-LB'), ('VJ6540-UB', 'VJ6530-UB'), ('VJ6541-LB', 'VJ6531-LB'), ('VJ6542-UB', 'VJ6532-UB'), ('VJ6543-LB', 'VJ6533-LB'), ('VJ6544-UB', 'VJ6534-UB')], max_length=64),
        ),
        migrations.AlterField(
            model_name='normal',
            name='Bus_number',
            field=models.CharField(choices=[('GT4500', 'GT4500'), ('GT4501', 'GT4501'), ('GT4502', 'GT4502'), ('GT4503', 'GT4503'), ('VJ6538-UB', 'VJ6528-UB'), ('VJ6539-LB', 'VJ6529-LB'), ('VJ6540-UB', 'VJ6530-UB'), ('WG6628-UB', 'WG6628-UB'), ('HY4555', 'HY4555'), ('HY4556', 'HY4556'), ('HY4557', 'HY4557'), ('HY4558', 'HY4558'), ('HY4559', 'HY4559'), ('HY4560', 'HY4560'), ('HY4561', 'HY4561'), ('WG6629-LB', 'WG6629-LB'), ('WG6630-UB', 'WG6630-UB'), ('WG6631-LB', 'WG6631-LB'), ('WG6632-UB', 'WG6632-UB'), ('WG6633-LB', 'WG6633-LB'), ('VJ6541-LB', 'VJ6531-LB'), ('VJ6542-UB', 'VJ6532-UB'), ('VJ6543-LB', 'VJ6533-LB'), ('VJ6544-UB', 'VJ6534-UB'), ('GT4504', 'GT4504'), ('GT4505', 'GT4505'), ('GT4506', 'GT4506'), ('GT4507', 'GT4507'), ('GT4508', 'GT4508'), ('GT4509', 'GT4509'), ('GT4510', 'GT4510'), ('GT4511', 'GT4511')], max_length=64),
        ),
        migrations.AlterField(
            model_name='premium',
            name='Bus_number',
            field=models.CharField(choices=[('WG6621-LB', 'WG6621-LB'), ('WG6622-UB', 'WG6622-UB'), ('WG6623-LB', 'WG6623-LB'), ('WG6624-UB', 'WG6624-UB'), ('WG6625-LB', 'WG6625-LB'), ('WG6626-UB', 'WG6626-UB'), ('GT4505', 'GT4505'), ('GT4506', 'GT4506'), ('GT4507', 'GT4507'), ('GT4508', 'GT4508'), ('VJ6537-LB', 'VJ6527-LB'), ('VJ6538-UB', 'VJ6528-UB'), ('VJ6539-LB', 'VJ6529-LB'), ('HY4555', 'HY4555'), ('HY4556', 'HY4556'), ('HY4557', 'HY4557'), ('HY4558', 'HY4558'), ('HY4559', 'HY4559'), ('HY4560', 'HY4560'), ('HY4561', 'HY4561'), ('VJ6540-UB', 'VJ6530-UB'), ('VJ6541-LB', 'VJ6531-LB'), ('VJ6542-UB', 'VJ6532-UB'), ('VJ6543-LB', 'VJ6533-LB'), ('VJ6544-UB', 'VJ6534-UB'), ('GT4509', 'GT4509'), ('GT4510', 'GT4510'), ('GT4511', 'GT4511'), ('WG6627-LB', 'WG6627-LB'), ('WG6628-UB', 'WG6628-UB'), ('WG6629-LB', 'WG6629-LB'), ('WG6630-UB', 'WG6630-UB'), ('WG6631-LB', 'WG6631-LB'), ('WG6632-UB', 'WG6632-UB'), ('WG6633-LB', 'WG6633-LB'), ('WG6634-UB', 'WG6634-UB')], max_length=64),
        ),
    ]
