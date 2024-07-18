from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0,
                                              max_digits=65)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('product_add_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='register_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]