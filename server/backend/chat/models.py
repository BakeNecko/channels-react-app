from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    rooms = models.ForeignKey(
        'Room', verbose_name='user_rooms', on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Room(models.Model):
    """
    A room for people to chat in.
    """
    title = models.CharField(max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id
