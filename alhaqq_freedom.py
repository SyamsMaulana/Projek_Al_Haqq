import os
import time

def alhaqq_freedom():
    os.system('clear')
    # --- PILAR ABSOLUT ---
    FAIR_RATE = 10000
    GOLD_USD_GRAM = 152.45  # Standar Global
    
    print("="*60)
    print("    AL-HAQQ ABSOLUTE REVO - FREEDOM & LEGACY ENGINE     ")
    print("      (Debt Clearance & Wedding Capital Protocol)       ")
    print("="*60)

    try:
        # 1. INPUT KURS (DETEKSI KEADILAN)
        current_usd = float(input("[>] Input Kurs USD/IDR Saat Ini: "))
        
        if current_usd > FAIR_RATE:
            print("\n" + "!"*60)
            print(" STATUS: HOLD / NO DEAL ")
            print(f" Kurs Rp {current_usd:,.0f} ZALIM. Tunggu Fair Value Rp 10.000.")
            print(" Melunasi/Membeli modal sekarang = Merugikan Aset Masa Depan!")
            print("!"*60)
            return

        # 2. INPUT DATA KEBUTUHAN
        pokok_hutang = float(input("\n[>] Total Sisa Pokok Hutang (Tanpa Bunga): Rp "))
        modal_nikah = float(input("[>] Target Modal Nikah Beradab: Rp "))
        
        total_kebutuhan_idr = pokok_hutang + modal_nikah
        
        # 3. KONVERSI KE STANDAR HAQQ (EMAS)
        harga_emas_haqq = GOLD_USD_GRAM * FAIR_RATE # Rp 1.524.500
        total_emas_needed = total_kebutuhan_idr / harga_emas_haqq
        
        # 4. MATRIKS 36% & 3% REWARD
        margin_36 = total_kebutuhan_idr * 0.36
        reward_adab_3 = total_kebutuhan_idr * 0.03

        print("\n" + "-"*60)
        print(f"[*] TOTAL KEBUTUHAN RIIL   : Rp {total_kebutuhan_idr:,.0f}")
        print(f"[*] SETARA BERAT EMAS      : {total_emas_needed:.2f} Gram")
        print(f"[*] MARGIN PERTAHANAN (36%): Rp {margin_36:,.0f}")
        print(f"[*] REWARD ADAB (3%)       : Rp {reward_adab_3:,.0f}")
        print("-" * 60)
        print(" STATUS: VALID - PROCEED WITH HONOUR ")

    except ValueError:
        print("\n[!] Error: Gunakan angka nominal saja.")

    print("\n" + "="*60)
    print("        OTENTIK ICAM/SYAMS MAULANA - AL-HAQQ         ")
    print("="*60)

if __name__ == "__main__":
    alhaqq_freedom()
