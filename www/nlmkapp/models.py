from django.db import models
from django.contrib import admin


# Create your models here.
class ObjectNLMK(models.Model):
    objectnlmk = models.CharField(max_length=250, blank=True, verbose_name='Объект', primary_key=True)
    bgp_as = models.CharField(max_length=10, verbose_name='AS')
    enterprise = models.CharField(max_length=250, blank=True, verbose_name='Предприятие')
    enterprise_addr = models.CharField(max_length=250, blank=True, verbose_name='Адрес предприятия')

    def __str__(self):
        return self.objectnlmk + ':' + self.bgp_as

    class Meta:
        verbose_name='Объект группы компаний'
        verbose_name_plural = "Объекты группы компаний"
 
        
class Operator(models.Model):
    operator = models.CharField(max_length=10, verbose_name='Код оператора', primary_key=True)
    operator_name = models.CharField(max_length=250, blank=True, verbose_name='Название оператора')

    def __str__(self):
        return self.operator_name

    class Meta:
        verbose_name='Оператор'
        verbose_name_plural = "Операторы"


class Channel(models.Model):
    ip = models.CharField(max_length=15, verbose_name='ip', primary_key=True)
    router = models.CharField(max_length=50, verbose_name='Имя роутера')
    operator = models.ForeignKey(Operator, verbose_name='Оператор', on_delete=models.CASCADE)
    bgp_as =  models.ForeignKey(ObjectNLMK, verbose_name='AS', on_delete=models.CASCADE)
    interface = models.CharField(max_length=50, verbose_name='Интерфейс/влан')
    pe = models.CharField(max_length=50, verbose_name='PE роутер')
    bandwidth = models.CharField(max_length=50, verbose_name='Ширина канала')
    address_channel = models.CharField(max_length=250, verbose_name='Адрес точки принятия канала')
    notes = models.CharField(max_length=250, verbose_name='Примечания')

    def __str__(self):
        return self.router

    class Meta:
        verbose_name='Канал'
        verbose_name_plural = "Каналы"

class Peering(models.Model):
    operator = models.ForeignKey(Operator, verbose_name='Оператор', on_delete=models.CASCADE)
    switch = models.CharField(max_length=50, blank=True, verbose_name='Свитч')
    port = models.CharField(max_length=50, blank=True, verbose_name='Порт свитча')
    bandwidth = models.CharField(max_length=50, blank=True, verbose_name='Ширина пиринга')
    contract = models.CharField(max_length=250, blank=True, verbose_name='Договор/Заказ')
    address_peering = models.CharField(max_length=250, verbose_name='Адрес пиринга')

    def __str__(self):
        return self.contract

    class Meta:
        verbose_name='Peering'
        verbose_name_plural = "Peerings"

class L3net(models.Model):
    operator = models.ForeignKey(Operator, verbose_name='Оператор', on_delete=models.CASCADE)
    network = models.CharField(max_length=250, blank=True, verbose_name='Пиринговая сеть')
    op_ip = models.GenericIPAddressField(verbose_name='IP оператора')
 #   op_ip = models.CharField(max_length=250, blank=True, verbose_name='IP оператора')
 #   out_ip = models.GenericIPAddressField(verbose_name='IP со стороны PSI')
    our_ip = models.CharField(max_length=250, blank=True, verbose_name='IP со стороны PSI')

    def __str__(self):
        return self.network

    class Meta:
        verbose_name='Сети стыков по L3'
        verbose_name_plural = "Сети стыков по L3"

class Type_channel(models.Model):
    operator =  models.ForeignKey(Operator, verbose_name='Код оператора', on_delete=models.CASCADE)
    type_channel = models.CharField(max_length=50, blank=True, verbose_name='Тип канала')

    def __str__(self):
        return self.type_channel

    class Meta:
        verbose_name='Тип канала'
        verbose_name_plural = "Типы каналов"


class Optelephone(models.Model):
    operator = models.ForeignKey(Operator, verbose_name='Оператор', on_delete=models.CASCADE)
    telephone = models.CharField(max_length=250, blank=True, verbose_name='Телефон оператора')

    def __str__(self):
        return self.telephone

    class Meta:
        verbose_name='Телефон оператора'
        verbose_name_plural = "Телефоны операторов"

class Opemail(models.Model):
    operator = models.ForeignKey(Operator, verbose_name='Оператор', on_delete=models.CASCADE)
    email =  models.EmailField(blank=True, verbose_name='Email оператора')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name='Email'


class Voipgw(models.Model):
    voip_ip = models.CharField(max_length=20, verbose_name='Ip voip gw')
    voip_gw = models.CharField(max_length=250, blank=True, verbose_name='Имя voip gw')
    objectnlmk = models.ForeignKey(ObjectNLMK, verbose_name='Объект', on_delete=models.CASCADE)

    def __str__(self):
        return self.voip_gw

    class Meta:
        verbose_name='Voip gw'


class Voipprefix(models.Model):
    prefix = models.CharField(max_length=10, verbose_name='Префикс')
    voipgw = models.ForeignKey(Voipgw, verbose_name='Имя voip gw', on_delete=models.CASCADE)
    width = models.CharField(max_length=250, blank=True, verbose_name='Длина префикса')

    def __str__(self):
        return self.prefix

    class Meta:
        verbose_name='Voip префикс'
        verbose_name_plural = "Voip префиксы"


class Clientcontact(models.Model):
    fio = models.CharField(max_length=59, verbose_name='ФИО')
    objectnlmk = models.ForeignKey(ObjectNLMK, verbose_name='object', on_delete=models.CASCADE)
    email = models.EmailField(blank=True, verbose_name='Email')
    telephone = models.CharField(max_length=250, blank=True, verbose_name='Телефон')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name='Контакты на местах'
        verbose_name_plural = "Контакты на местах"
