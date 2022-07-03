from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.text import slugify

from accounts.enums import RoleCodes

from django.core.validators import MinValueValidator
from .validators import ENGLISH_REGEX_VALIDATOR


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField("نام کاربری", max_length=30, unique=True, validators=[ENGLISH_REGEX_VALIDATOR])
    email = models.EmailField('ایمیل', unique=True, null=True, blank=True)
    role = models.ForeignKey(
        'Role', on_delete=models.DO_NOTHING, verbose_name="نقش")
    favourites = models.ManyToManyField('Commodity', verbose_name='کالاهای مورد علاقه')

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "کاربر"
        verbose_name = "کاربر"

    from accounts.managers import UserManager
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

   # def is_seller(self):
    #    return self.role.code == RoleCodes.SELLER.value

    def is_admin(self):
        return self.role.code == RoleCodes.ADMIN.value

    def is_normal(self):
        return self.role.code == RoleCodes.NORMAL.value

    def is_staff(self):
        return True


class Role(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField("کد", max_length=10, unique=True, validators=[ENGLISH_REGEX_VALIDATOR])
    title = models.CharField("عنوان", max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "نقش"
        verbose_name = "نقش"


class Category(models.Model):
    title = models.CharField("عنوان", max_length=30, unique=True)
    parent = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name="دسته بندی پدر")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "دسته بندی"
        verbose_name = "دسته بندی"


class Commodity(models.Model):
    title = models.CharField("عنوان", max_length=30)
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING, verbose_name="دسته بندی")
    amount = models.FloatField("مبلغ", default=float(0),
                               validators=[MinValueValidator(0)]
                               )
    created_at = models.DateTimeField("تاریخ ثبت", auto_now_add=True)
    image = models.ImageField(
        upload_to='image/', default='defaults/commedity.jpg')
    shops = models.ManyToManyField('Shop',verbose_name='فروشندگان')
    features = models.ManyToManyField('Feature',verbose_name='ویژگی ها')

    class Meta:
        verbose_name_plural = "کالا"
        verbose_name = "کالا"

    def __str__(self):
        return self.title



class Shop(models.Model):
    title = models.CharField("عنوان", max_length=30)
    class Meta:
        verbose_name_plural = "فروشنده"
        verbose_name = "فروشنده"

    def __str__(self):
        return self.title

class Feature(models.Model):
    title = models.CharField("عنوان", max_length=30)
    description = models.CharField("عنوان", max_length=30)

    class Meta:
        verbose_name_plural = "ویژگی"
        verbose_name = "ویژگی"

    def __str__(self):
        return self.title