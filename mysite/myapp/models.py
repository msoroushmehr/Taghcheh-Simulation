from tabnanny import verbose
from turtle import update
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.utils.html import format_html
from jalaliconv.utils import jalali_convertor
from jalaliconv.utils import numbers_convertor
from django.db.models import Count

class User(AbstractUser):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربرها"
        
        

class MyIPAddress(models.Model):
    ip_address = models.GenericIPAddressField()
        

class BookManager(models.Manager):
    def published(self):
        return self.filter(status="p")
    
    
class CategoryManager(models.Manager):
    def published(self):
        return self.filter(status="p")
    
    
    
    
   
    
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    mtitle = models.CharField(max_length=200, null=True, blank=True, verbose_name="  عنوان در سایت")
    msubtitle = models.CharField(null=True, blank=True,max_length=200, verbose_name="زیرعنوان در سایت")
    description = models.TextField(null=True, blank=True,verbose_name="محتوا در سایت")
    parent = models.ForeignKey('self',blank=True, default=None, null=True, on_delete=models.SET_NULL, verbose_name="زیردسته", related_name='child')
    slug = models.SlugField(max_length=100,unique=True, verbose_name="اسلاگ")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    image = models.ImageField(upload_to="Images", null=True, blank=True,  verbose_name="تصویر")
    position = models.IntegerField()
    
    objects = BookManager()  

    def __str__(self):
        return self.title   
    

    def pdescription(self):
        return numbers_convertor(self.description)
    
    
    
    


    class Meta:
        ordering = ['position']
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

class Publication(models.Model):
    class Meta:
        verbose_name = "ناشر"
        verbose_name_plural = "ناشران"
       
    title = models.CharField(max_length=200, verbose_name="نام ناشر")
    
    
    def __str__(self):
        return self.title
    
            





     

class Book(models.Model):
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتابها"
    STATUS_CHOICES = [('d', 'پیش نویس'), ('p', 'چاپ شده')]
    title = models.CharField(max_length=200, verbose_name="عنوان کتاب")
    subtitle = models.CharField(max_length=300, null=True, blank=True, verbose_name="توضیح عنوان")
    description = models.TextField(verbose_name="محتوا")
    slug = models.SlugField(max_length=100,unique=True, verbose_name="اسلاگ")
    image = models.ImageField(upload_to="Images", verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضغیت انتشار")
    publication = models.ForeignKey(Publication, null=True, on_delete=models.CASCADE, verbose_name="ناشر")
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='books')
    author = models.CharField(max_length=200, verbose_name='نویسنده کتاب')
    mauthor = models.CharField(max_length=200, null=True, blank=True, verbose_name='گردآورنده')
    price = models.IntegerField(verbose_name="قیمت")
    disscount = models.BigIntegerField(null=True, blank=True, verbose_name="درصد تخفیف")
    time_disscount = models.DateTimeField(default=timezone.now, verbose_name=" تخفیف تا ")
    # hits = models.ManyToManyField(IPAddress, blank=True, related_name="hits", verbose_name="بازدیدها")

    # def get_client_ip(self, request):
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip

    #     Bview.objects.get_or_create(user=self.request.user, book=self.book_details)

    def countv(self):
        return self.hits.all.count()
    
    
    def category_to_str(self):
        return ",".join([category.title for category in self.category.all()])
    
    category_to_str.short_description = "دسته بندی"
    
    def __str__(self):
        return self.title
        
    def category_to_list(self):
        return list(self.category_to_str().split(","))
    
    def image_tag(self):
        return format_html("<img width=100 height=75 src='{}'>".format(self.image.url))
    
   
    def jpublish(self):
        return jalali_convertor(self.publish)
    
    def pdescription(self):
        return numbers_convertor(self.description)
    
    def pprice(self):
        
        return numbers_convertor(str(self.price))

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    
    objects = BookManager()   

   
class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    body = models.TextField(default=None,verbose_name="متن نظر")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'دیدگاه {}'.format(self.name)
    
    def jpublish(self):
        return jalali_convertor(self.created_on)





    