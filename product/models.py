from django.db import models
from django.utils import html

class Category(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='نام دسته')
    parent = models.ForeignKey('self', verbose_name='دسته مادر', \
            on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='children')

    class Meta:

        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها '

    def __str__(self):
        return self.name

class Product(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='نام محصول')
    category = models.ForeignKey(Category, verbose_name='نام ذسته', on_delete=models.CASCADE, related_name='categories')
    image = models.ImageField(upload_to='media', verbose_name='تصویر محصول')
    count = models.PositiveIntegerField(verbose_name='تعداد ')
    type = models.CharField(max_length=20, verbose_name='نوع')
    size = models.CharField(max_length=20, verbose_name='اندازه')
    price = models.PositiveIntegerField(verbose_name='قیمت خرید')
    sale_price = models.PositiveIntegerField(verbose_name='قیمت فروش')
    description = models.TextField(verbose_name='توضیحات محصول')

    class Meta:

        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name

    def category_to_str(self):
         return " - ".join([category.title for category in self.category.all()])
    category_to_str.short_description = 'دسته بندی'

    def image_tag(self):
         return html.format_html("<img width=100; height=75; style='border-radius:10px;'src='{}'>".format(self.image.url))
    image_tag.short_description = short_decsription = 'تصویر محصول'