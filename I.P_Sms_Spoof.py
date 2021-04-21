#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from os import system as s



banner = """
                            
┌───── •✧✧• ─────┐
 IllegalPlatform 
└───── •✧✧• ─────┘                                                                                                     
                                                                                                                                
|Sms Spoofing Tool - İllegalPlatform.com 
|Keremsanti tarafından türkçeleştirildi. Tool bana ait değildir.
|Bilgi:
|Günlük Limitin : 1
|Mesajını Çok Uzun Karakter Tutma
|Telefon Numarasını +90 Şeklinde Doğru Yaz

"""

print(banner)

sor = input("Gönderilecek Telefon Numarası : Örn:+905***** >>> ")

mesaj = input("Mesajınız >>> ")

arlk = mesaj[0:70]

print("\n| Gönderlicek Mesajın Taslağı aşagıdaki gibidir.\n"+arlk)

drlm = input("\n| Mesajın Gönderilmesini Onaylıyor musunuz ? [y/n] >>> ")

if drlm == "y" or drlm == "Y":
    print("\n"+sor+"\n"+arlk+"\n")
    resp = requests.post('https://textbelt.com/text', {
  'phone': sor,
  'message': arlk,
  'key': 'textbelt',
    })
    print(resp.json())

elif drlm == "n" or drlm == "N":
    quit()
else:
    print("\n|Hatalı Format.")

