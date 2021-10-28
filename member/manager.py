from django.contrib.auth.models import UserManager

class UserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **kwargs):

        if not phone_number:
            raise ValueError("Phone number must be provided")

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, phone_number, password=None, **kwargs):
        kwargs.setdefault('is_superuser', False)
        
        return self._create_user(phone_number, password, **kwargs)

    def create_superuser(self, phone_number, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)

        if kwargs.get('is_superuser') is not True:
            raise ValueError("Superuser must be is_superuser=True.")

        return self._create_user(phone_number, password, **kwargs)
        

