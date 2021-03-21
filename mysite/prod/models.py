from django.conf import settings
from django.db import models
from django.utils import timezone
 

class Zakaz(models.Model):
    nom_zak = models.IntegerField(default="№")                                      #номер заказа
    title = models.CharField(max_length=200, default="клиент")                      #клиент
    text = models.TextField(default="комментарий")                                  #комментарий
    start_date = models.DateTimeField(default=timezone.now)                         #дата начала
    finish_date = models.DateTimeField(default=timezone.now)                        #дата завершения
    status = models.CharField(max_length=20)                                        #статус (в работе/выполнен/отгружен/монтаж и т.д.)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                            #автор 
    created_date = models.DateTimeField(default=timezone.now)                       #дата создания

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
        
    class Meta:
    	verbose_name = 'Заказ'
    	verbose_name_plural = 'Заказы'



class Detal(models.Model):
    detal_title = models.CharField(max_length=200)                                  #название
    detal_size = models.IntegerField()                                              #размер
    detal_weight = models.IntegerField()                                            #вес
    detal_text = models.CharField(max_length=200, default="описание")               #описание
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)                            #создатель 
    created_date = models.DateTimeField(default=timezone.now)                       #дата создания
    detal_status = models.CharField(max_length=20)                                  #статус используется или нет

    def publish(self):
        self.save()

    def __str__(self):
        return self.detal_title
        
    class Meta:
        verbose_name = 'Деталь'
        verbose_name_plural = 'Детали'