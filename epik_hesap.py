#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Ciddi ve Abartılı Hesap Makinesi
Sadece toplama yapar. Ama destan yazar.
"""

import time
import random

def destan_yaz(a, b, toplam):
    destanlar = [
        f"{a} ve {b} sayıları, evrenin başlangıcından beri birbirlerini arıyorlardı. Nihayet buluştular ve {toplam} oldular. Bu birleşme, galaksileri titretti.",
        f"Tarih kitapları {a} + {b} = {toplam} diye yazacak. Çünkü bu sadece matematik değil, bir destandır.",
        f"{a} sayısı {b}'ye baktı ve dedi ki: 'Sen olmadan ben eksiktim.' Sonra {toplam} oldular. Gözyaşları aktı.",
        f"Bu toplama işlemi o kadar ciddidir ki, NASA bile izliyor. Sonuç: {toplam}. Dünya kurtuldu."
    ]
    return random.choice(destanlar)

def main():
    print("=" * 60)
    print("EPİK HESAP MAKİNESİ - DÜNYANIN EN CİDDİ TOPLAMA ARACI")
    print("=" * 60)
    print("Uyarı: Bu program o kadar ciddidir ki, yanlış sayı girerseniz evren çökebilir.")
    print()
    
    try:
        a = float(input("Birinci sayıyı girin (ciddiyetle): "))
        b = float(input("İkinci sayıyı girin (abartıyla): "))
        
        print("\nHesaplanıyor... (destan yazılıyor)")
        time.sleep(1.5)
        
        toplam = a + b
        
        print("\n" + "-" * 60)
        print(destan_yaz(a, b, toplam))
        print("-" * 60)
        print(f"\nSONUÇ (ciddi): {toplam}")
        print("\nTebrikler. Bir çağı kapattınız.")
        
        # gizli not: bu yorumun içinde gizli bir mesaj var. base64: QWRhIGFuYXNheWEga2ltaXNlIHZhcg==  (sadece şaka, saklama)
        
    except ValueError:
        print("Hata: Sayı girmeniz gerekiyordu. Evren şimdilik kurtuldu.")

if __name__ == "__main__":
    main()

# Damga: Grok Kayyum | Tarih: 2026-10-25 | İmza: Kayyum Grok
