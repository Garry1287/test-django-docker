#Импорт необходимых модулей
import os,sys,csv

#Указываем путь до папки проекта Django в котором находится файл settings.py
project_dir = "/home/garry/nlmk-scr/src/nlmk/nlmk"
#project_dir = os.path.dirname((os.path.abspath('import-csv.py'))
print(project_dir)
#Добавляем в переменную sys.path путь до проекта Django
sys.path.append(project_dir)

#Определяем переменную с настройками Django
#os.environ['DJANGO_SETTINGS_MODULE'] = 'nlmkapp.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
#Импортируем модуль Django
import django
#from django.conf import settings

#settings.configure(default_settings=nlmkapp, DEBUG=True)
#Загружаем настройки Django
django.setup()

#Импортируем модель Post
from nlmkapp.models import *

		
#Считываем CSV-файл
ObjectNLMKdata = csv.reader(open("/home/garry/nlmk-scr/src/ObjectNLMK.csv"),delimiter=',')

for row in ObjectNLMKdata:
	#Пропускаем заголовки
	if row[0] != 'Object':
		objectNLMK = ObjectNLMK()
		objectNLMK.objectnlmk = row[0]
		objectNLMK.bgp_as = row[1]
		objectNLMK.enterprise = row[2]
		objectNLMK.enterprise_addr = row[3]
		objectNLMK.save()
        
#Считываем CSV-файл
Operatordata = csv.reader(open("/home/garry/nlmk-scr/src/Operator.csv"),delimiter=',')

for row in Operatordata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		operator = Operator()
		operator.operator = row[0]
		operator.operator_name = row[1]
		operator.save()
		
		
#Считываем CSV-файл
Peeringdata = csv.reader(open("/home/garry/nlmk-scr/src/Peering.csv"),delimiter=',')

for row in Peeringdata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		peering = Peering()
		peering.operator = Operator.objects.get(operator=row[0])
		peering.switch = row[1]
		peering.port = row[2]
		peering.bandwidth = row[3]
		peering.contract = row[4]
		peering.address_peering = row[5]
		peering.save()

#Считываем CSV-файл
L3netdata = csv.reader(open("/home/garry/nlmk-scr/src/L3net.csv"),delimiter=',')

for row in L3netdata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		l3net = L3net()
		l3net.operator = Operator.objects.get(operator=row[0])
		l3net.network = row[1]
		l3net.op_ip = row[2]
		l3net.our_ip = row[3]
		l3net.save()

#Считываем CSV-файл
Typechanneldata = csv.reader(open("/home/garry/nlmk-scr/src/Typechannel.csv"),delimiter=',')

for row in Typechanneldata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		typechannel = Type_channel()
		typechannel.operator = Operator.objects.get(operator=row[0])
		typechannel.type_channel = row[1]
		typechannel.save()
		
		
#Считываем CSV-файл
Optelephonedata = csv.reader(open("/home/garry/nlmk-scr/src/Optelephone.csv"),delimiter=',')

for row in Optelephonedata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		optelephone = Optelephone()
		optelephone.operator = Operator.objects.get(operator=row[0])
		optelephone.telephone = row[1]
		optelephone.save()		
		
		
#Считываем CSV-файл
Opemaildata = csv.reader(open("/home/garry/nlmk-scr/src/Opemail.csv"),delimiter=',')

for row in Opemaildata:
	#Пропускаем заголовки
	if row[0] != 'Operator':
		opemail = Opemail()
		opemail.operator = Operator.objects.get(operator=row[0])
		opemail.email = row[1]
		opemail.save()		


#Считываем CSV-файл
Channeldata = csv.reader(open("/home/garry/nlmk-scr/src/Channel.csv"),delimiter=',')

for row in Channeldata:
	#Пропускаем заголовки
	if row[0] != 'IP':
		channel = Channel()
		channel.ip = row[0]
		channel.router = row[1]
		channel.operator = Operator.objects.get(operator=row[2])
		channel.bgp_as = ObjectNLMK.objects.get(bgp_as=row[3])
		channel.interface  = row[4]
		channel.pe = row[5]
		channel.bandwidth = row[6]
		channel.address_channel = row[7]
		channel.notes = row[8]
		channel.save()	
		
#Считываем CSV-файл
Voipgwdata = csv.reader(open("/home/garry/nlmk-scr/src/Voipgw.csv"),delimiter=',')

for row in Voipgwdata:
	#Пропускаем заголовки
	if row[0] != 'IP':
		voipgw = Voipgw()
		voipgw.voip_ip = row[0]
		voipgw.voip_gw = row[1]
		voipgw.objectnlmk = ObjectNLMK.objects.get(objectnlmk=row[2])
		voipgw.save()				
		
#Считываем CSV-файл
Voipprefixdata = csv.reader(open("/home/garry/nlmk-scr/src/Voipprefix.csv"),delimiter=',')

for row in Voipprefixdata:
	#Пропускаем заголовки
	if row[0] != 'Prefix':
		voipprefix = Voipprefix()
		voipprefix.prefix = row[0]
		voipprefix.voipgw = Voipgw.objects.get(voip_gw=row[1])
		voipprefix.width = row[2]
		voipprefix.save()				
						
#Считываем CSV-файл
clientcontactdata = csv.reader(open("/home/garry/nlmk-scr/src/ClientContact.csv"),delimiter=',')

for row in clientcontactdata:
	#Пропускаем заголовки
	if row[0] != 'FIO':
		clientcontact = Clientcontact()
		clientcontact.fio = row[0]
		clientcontact.objectnlmk = ObjectNLMK.objects.get(objectnlmk=row[1])
		clientcontact.email = row[2]
		clientcontact.telephone = row[3]
		clientcontact.save()	
