from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, phone_number, password=None):
        if not email:
            return ValueError("user must have an email address")

        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, password=None):
        user = self.create_user(email, phone_number, password)
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
