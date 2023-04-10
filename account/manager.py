from django.contrib.auth.models import BaseUserManager


class AccoutManager(BaseUserManager):

    # simple user
    def create_user(self, phone_number, last_name, first_name, password=None):
        if not phone_number:
            raise ValueError("phone_number is required")
        if not last_name:
            raise ValueError("Username is required")

        user = self.model(
            phone_number=phone_number,
            last_name=last_name,
            first_name=first_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    # superuser
    def create_superuser(self, phone_number, first_name, last_name, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            last_name=last_name,
            first_name=first_name,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
