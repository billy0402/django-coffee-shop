from django.db import models


# Create your models here.
class Roast(models.TextChoices):
    # enum = value, display
    LIGHT = 'Light', '極淺度烘焙'
    CINNAMON = 'Cinnamon', '淺度烘焙'
    MEDIUM = 'Medium', '中度烘焙'
    HIGH = 'High', '中度微深烘焙'
    CITY = 'City', '中深度烘焙'
    FULL_CITY = 'Full-City', '微深度烘焙'
    FRENCH = 'French', '極深烘焙'
    ITALIAN = 'Italian', '極深度烘焙'


class OriginPlace(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '產地'
        verbose_name_plural = '產地'


class MainProcessing(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '主要處理法'
        verbose_name_plural = '主要處理法'


class Grinding(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '磨豆方式'
        verbose_name_plural = '磨豆方式'


class Coffee(models.Model):
    name = models.CharField('名稱', max_length=20, unique=True)
    weight = models.PositiveIntegerField('重量')
    taste = models.TextField('味道')
    description = models.TextField('描述')
    roast = models.CharField('烘培程度', max_length=10, choices=Roast.choices)
    price = models.PositiveIntegerField('價格')
    discount = models.PositiveIntegerField('優惠價格')
    origin_place = models.ForeignKey(
        OriginPlace,
        on_delete=models.PROTECT,
        verbose_name='產地',
    )
    main_processing = models.ForeignKey(
        MainProcessing,
        on_delete=models.PROTECT,
        verbose_name='主要處理法',
    )
    grindings = models.ManyToManyField(Grinding, verbose_name='磨豆方式')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '咖啡'
        verbose_name_plural = '咖啡'
