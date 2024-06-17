from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomStoreManager(BaseUserManager):
    def create_user(self, store_code, password=None, **extra_fields):
        if not store_code:
            raise ValueError(_('The Store Code field must be set'))
        
        user = self.model(store_code=store_code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, store_code, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        return self.create_user(store_code, password, **extra_fields)

class Store(AbstractBaseUser, PermissionsMixin):
    store_code = models.CharField(
        max_length=4,
        unique=True,
        verbose_name=_('store code')
    )
    is_staff = models.BooleanField(
        verbose_name=_('staff status'),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_("created at"),
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name=_("updated at"),
        auto_now=True
    )

    objects = CustomStoreManager()

    USERNAME_FIELD = 'store_code'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.store_code

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")