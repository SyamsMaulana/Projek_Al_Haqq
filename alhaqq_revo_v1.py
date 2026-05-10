import os

def al_haqq_update():
    os.system('clear')
    print("="*55)
    print("   UPDATE PROTOKOL: AL-HAQQ ABSOLUTE REVO v1.0   ")
    print("      (Standard: Gold & Silver Real-Time)      ")
    print("="*55)
    print("[!] INSTRUKSI: Gunakan Akal, Bukan Nafsu.")
    
    try:
        # Konversi Riil
        harga_emas = float(input("\n[>] Update Harga Emas Hari Ini (Rp/gr): "))
        aset_gram = float(input("[>] Total Target Aset (dalam Gram Emas): "))
        
        # 36% Filter Rasionalitas
        min_deposit = aset_gram * 0.36
        red_line = aset_gram * 0.12
        cashback_adab = aset_gram * 0.03

        print("\n" + "-"*55)
        print(f"[*] TOTAL TARGET ASET  : {aset_gram:.2f} gr Emas")
        print(f"[*] SYARAT MASUK (36%) : {min_deposit:.2f} gr Emas")
        print(f"[*] BATAS KRITIS (12%) : {red_line:.2f} gr Emas")
        print(f"[*] REWARD ADAB (3%)   : {cashback_adab:.2f} gr Emas")
        print("-" * 55)
        
        print("\n[PESAN UNTUK TIS]")
        print("> 92% Struktur ini adalah Harga Mati.")
        print("> Gunakan 8% Anda untuk efisiensi instrumen investasi.")
        print("> Membangun Masa Depan = Memuliakan Kejujuran.")

    except ValueError:
        print("[!] Gunakan angka yang valid untuk kalkulasi Al-Haqq.")

    print("\n" + "="*55)
    print("   OTENTIK ICAM/SYAMS MAULANA - AL-HAQQ PROTOCOL   ")
    print("="*55)

if __name__ == "__main__":
    al_haqq_update()
