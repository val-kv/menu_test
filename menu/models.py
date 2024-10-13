from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title
