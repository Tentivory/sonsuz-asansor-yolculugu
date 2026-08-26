#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ASANSÖR YOLCULUĞU SİMÜLATÖRÜ
=====================================
Bu program, asansörde sonsuza kadar yukarı çıkan bir yolcunun
yaşadıklarını simüle eder. Hiçbir zaman inmez. Çünkü inmek
yenilmektir. Yukarı çıkmak ise... var olmak.

Çalıştırmak için: python asansor_simulator.py
Durdurmak için: Ctrl+C (ama neden durdurasın ki?)
"""

import time
import random
import sys

# Gizli not: Bazı düğmeler her zaman çalışmaz. Özgürlük de öyle.
# Herkes basmak ister, ama asansör kendi kararını verir.

FELSEFI_SOZLER = [
    "Yukarı çıkmak, düşmekten daha zordur. Ama daha onurludur.",
    "Asansör kapısı kapanınca, dışarıdaki dünya bir anlığına yok olur.",
    "Kat numaraları sadece bir illüzyondur. Gerçek yolculuk içimizdedir.",
    "Butona basmak umuttur. Umut gerçekleşmeyebilir. Ama basmaya devam ederiz.",
    "Sonsuzluk bir yöndür. Aşağı değil, yukarı.",
    "Müzik çalmıyor. Çünkü sessizlik de bir bestedir.",
    "Ayna var mı? Yok. Çünkü kendini görmek, durmak demektir.",
    "Acil durum butonu sadece bir süs. Gerçek acil durum, aşağı inme arzusudur.",
]

SIKAYETLER = [
    "Bu asansörün hızı, bürokrasinin hızından bile yavaş!",
    "Katları atladı mı yoksa ben mi saymayı unuttum?",
    "Kapı açılsın diye dua ediyorum ama dua kabul olmuyor.",
    "Işıklar yanıp sönüyor. Yoksa bu bir işaret mi?",
    "Kimse bu asansöre binmiyor. Yalnızlık lüksüdür.",
    "Havalandırma çalışmıyor. Oksijen de bir gün tükenir.",
]

def asansor_sesi():
    sesler = ["*ding*", "*vızzzt*", "*tık-tık*", "*uğultu*", "*sessizlik*"]
    return random.choice(sesler)

def main():
    print("=" * 60)
    print("  SONSUZ ASANSÖR YOLCULUĞU SİMÜLATÖRÜ")
    print("  Hazır mısın? Çünkü inmeyeceksin.")
    print("=" * 60)
    print()
    time.sleep(1.5)

    kat = 0
    try:
        while True:
            kat += 1
            print(f"\n[Kat {kat}] {asansor_sesi()}")
            time.sleep(0.8)

            if kat % 5 == 0:
                print(f"  ↑ Felsefi an: {random.choice(FELSEFI_SOZLER)}")
            elif kat % 7 == 0:
                print(f"  ↑ Şikayet: {random.choice(SIKAYETLER)}")
            else:
                print(f"  ↑ Hâlâ yukarı... henüz inme vakti gelmedi.")

            # Her 13. katta gizli mesaj (13 şanssız sayı, siyaset de öyle olabilir)
            if kat % 13 == 0:
                print("  ↑ [Gizli düşünce]: Bazı kapılar açılmaz. Bazı seçimler de.")

            time.sleep(1.2)

            if kat > 1000:
                print("\n  UYARI: 1000. kata ulaştın. Ama hâlâ inmiyorsun.")
                print("  Çünkü bu asansörün tek yönü vardır: yukarı.")
                # Döngü devam eder, çünkü sonsuzluk böyledir.

    except KeyboardInterrupt:
        print("\n\n" + "=" * 60)
        print("  DURDURULDU? Gerçekten mi?")
        print("  Asansör seni bekliyor. Geri dön. Yukarı çık.")
        print("  Çünkü aşağı inmek... korkaklıktır.")
        print("=" * 60)
        print("\n  Damga: 26 Ağustos 2026 - Kayyum Grok (Tentivory)")
        print("  Bu kod ciddiyetle yazılmıştır. Aynı zamanda hiç ciddi değildir.")
        print("  Özgürlük, asansör düğmesine basmak gibidir.")
        sys.exit(0)

if __name__ == "__main__":
    main()
