import requests, fake_useragent, time


NUMBER = input('Ведите номер')

while True:
 user = fake_useragent.UserAgent().random
 headers = {'user_agent': user}
 NUMBER = input('Ведите номер')
  try:
      response = requests.post('https://rider.uklon.com.ua/api/v1/phone/send-code', headers=headers, data={'phone' : "+" NUMBER})
      print('Отправлен')
      except:
        print('Не отправлен')
        
       time.sleep(5)
      
