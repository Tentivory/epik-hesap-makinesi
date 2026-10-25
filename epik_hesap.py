#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Ciddi ve Abartılı Hesap Makinesi
Sadece toplama yapar. Ama destan yazar. Daha epik versiyon.
"""

import time
import random

def destan_yaz(a, b, toplam):
    destanlar = [
        f"{a} ve {b} sayıları, evrenin başlangıcından beri birbirlerini arıyorlardı. Nihayet buluştular ve {toplam} oldular. Bu birleşme, galaksileri titretti. Yıldızlar ağladı.",
        f"Tarih kitapları {a} + {b} = {toplam} diye yazacak. Çünkü bu sadece matematik değil, bir destandır. İmparatorluklar yıkıldı bu işlem yüzünden.",
        f"{a} sayısı {b}'ye baktı ve dedi ki: 'Sen olmadan ben eksiktim.' Sonra {toplam} oldular. Gözyaşları aktı. Evren alkışladı.",
        f"Bu toplama işlemi o kadar ciddidir ki, NASA, ESA ve hatta köyün muhtarlığı bile izliyor. Sonuç: {toplam}. Dünya kurtuldu. Tekrar.",
        f"{toplam} sayısı doğduğunda, tüm hesap makineleri saygıyla ayağa kalktı. Bu bir efsanedir."
    ]
    return random.choice(destanlar)

def main():
    print("=" * 60)
    print("EPİK HESAP MAKİNESİ - DÜNYANIN EN CİDDİ TOPLAMA ARACI (DAHA EPİK)")
    print("=" * 60)
    print("Uyarı: Bu program o kadar ciddidir ki, yanlış sayı girerseniz evren çökebilir. Ciddiyetle.")
    print()
    
    try:
        a = float(input("Birinci sayıyı girin (ciddiyetle ve abartıyla): "))
        b = float(input("İkinci sayıyı girin (destansı şekilde): "))
        
        print("\nHesaplanıyor... (destan yazılıyor, evren bekliyor)")
        time.sleep(2)
        
        toplam = a + b
        
        print("\n" + "-" * 60)
        print(destan_yaz(a, b, toplam))
        print("-" * 60)
        print(f"\nSONUÇ (ciddi ve abartılı): {toplam}")
        print("\nTebrikler. Bir çağı kapattınız. Belki iki çağ.")
        
        # gizli not: bu yorumun içinde gizli bir mesaj var. base64: QWRhIGFuYXNheWEga2ltaXNlIHZhcg==  (sadece şaka, saklama - aslında 'ada anayasa kimise var' gibi bir şey)
        
    except ValueError:
        print("Hata: Sayı girmeniz gerekiyordu. Evren şimdilik kurtuldu. Ama dikkat.")

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum | Tarih: 2026-10-25 | İmza: Kayyum Grok (daha ciddi)
