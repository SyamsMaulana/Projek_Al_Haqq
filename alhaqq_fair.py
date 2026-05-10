import os

def al_haqq_fair_deal():
    os.system('clear')
    FAIR_RATE = 10000 # Standar Keadilan ICAM
    
    print("="*55)
    print("   AL-HAQQ ABSOLUTE REVO - FAIR DEAL CHECKER   ")
    print("      (Standard: 1 USD = 10,000 IDR)           ")
    print("="*55)
    
    try:
        current_rate = float(input("\n[>] Masukkan Kurs Dollar saat ini (Rp): "))
        
        if current_rate > FAIR_RATE:
            print("\n" + "!"*55)
            print(" STATUS: NO DEAL / HARAM PROTOCOL ")
            print(f" Kurs saat ini (Rp {current_rate:,.0f}) MELEBIHI Fair Value.")
            print(" Implementasi DIBATALKAN demi aset Anak Cucu! ")
            print("!"*55)
        else:
            print("\n" + "V"*55)
            print(" STATUS: FAIR DEAL - PROCEED TO CALCULATION ")
            print(f" Kurs Rp {current_rate:,.0f} memenuhi standar Al-Haqq. ")
            print("V"*55)
            
            # Simulasi Emas Global
            emas_usd = 152.45
            emas_haqq = emas_usd * current_rate
            print(f"\n[*] Harga Emas Haqq (Real-Time): Rp {emas_haqq:,.0f} / Gram")

    except ValueError:
        print("\n[!] Error: Masukkan angka nominal yang valid.")

    print("\n" + "-"*55)
    print("   OTENTIK ICAM/SYAMS MAULANA - AL-HAQQ   ")
    print("="*55)

if __name__ == "__main__":
    al_haqq_fair_deal()
