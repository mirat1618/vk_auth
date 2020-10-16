import requests
import re
from getpass import getpass

email = input('Введите логин(номер телефона или e-mail): ')
password = getpass('Введите пароль: ')

s = requests.Session()
url = 'https://login.vk.com'
r = s.get ('https://m.vk.com')
with open ('vk.txt', 'w') as file:
    file.write(r.text)
    
text = r.text

act_pattern = re.compile('act=(.{1,})&_')
act = act_pattern.findall(text)[0]

origin_pattern = re.compile('origin=(.{1,})&ip')
origin = origin_pattern.findall(text)[0]

iph_pattern = re.compile('ip_h=(.{1,})&lg')
ip_h = iph_pattern.findall(text)[0]

lgh_pattern = re.compile('lg_h=(.{1,})&ro')
lg_h = lgh_pattern.findall(text)[0]

role_pattern = re.compile('role=(.{1,})&ut')
role = role_pattern.findall(text)[0]

utf_pattern = re.compile('tf8=(.{1,})"')
utf = utf_pattern.findall(text)[0]

print ('act = ', act,
'\norigin = ', origin,
'\nip_h = ', ip_h,
'\nlg_h = ', lg_h,
'\nrole = ', role,
'\nutf-8', utf)

data = {'email' : email,
'pass': password,
'act': 'login',
'_origin': 'https://m.vk.com',
'ip_h' : ip_h,
'role' : 'pda' ,
'lg_h': lg_h,
'utf8' : '1'}

r = s.post (url, data = data)
r = s.get('https://m.vk.com/mail')
print (r.content)
