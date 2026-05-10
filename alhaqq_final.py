import os
import time

def main_protocol():
    os.system('clear')
    # --- KONSTRUKSI KEADILAN (92% LOCKED) ---
    FAIR_USD_RATE = 10000
    GOLD_GLOBAL_USD = 152.45
    EXPECTED_GOLD_IDR = GOLD_GLOBAL_USD * FAIR_USD_RATE # Rp 1.524.500

    print("="*60)
    print("      AL-HAQQ ABSOLUTE REVO - INTEGRITY ENGINE v1.0      ")
    print("        (Anti-Manipulation & Eternal Value Mode)         ")
    print("="*60)

    try:
        # 1. CEK KURS DOLLAR
        current_usd = float(input("[>] Input Kurs USD/IDR Saat Ini: "))
        
        # 2. CEK HARGA EMAS (Untuk Deteksi Redenomasi)
        current_gold = float(input("[>] Input Harga Emas per Gram (Rp): "))

        print("\n" + "~"*60)
        print("[*] Melakukan Validasi Integritas Moneter...")
        time.sleep(1)

        # LOGIKA ANTI-MANIPULASI
        # Jika kurs terlihat murah (<=10k) tapi harga emas masih jutaan, itu manipulasi nol!
        if current_usd <= FAIR_USD_RATE and current_gold > (EXPECTED_GOLD_IDR * 1.2):
            print("\n[!!!] STATUS: DETEKSI MANIPULASI (REDENOMASI)")
            print("[!] Angka nol mungkin dihilangkan, tapi daya beli tetap lemah.")
            print("[!] KEADILAN RIIL BELUM TERCAPAI. STATUS: NO DEAL.")
            print("~"*60)
            return

        # LOGIKA HARD-GATE KURS
        if current_usd > FAIR_USD_RATE:
            print("\n[!!!] STATUS: NO DEAL / HARAM PROTOCOL")
            print(f"[!] Kurs Rp {current_usd:,.0f} melebihi Fair Value Rp {FAIR_USD_RATE:,.0f}.")
            print("[!] Menunggu Keadilan Moneter untuk Implementasi TIS.")
            print("~"*60)
            return

        # JIKA LOLOS SEMUA FILTER (FAIR DEAL)
        print("\n[V] STATUS: FAIR DEAL & AUTHENTIC VALUE")
        print("[*] Menghitung Matriks Al-Haqq untuk Aset Anda...")
        
        total_aset_gram = float(input("\n[>] Masukkan Target Luas/Nilai Aset (Gram Emas): "))
        
        nilai_riil = total_aset_gram * current_gold
        margin_36 = nilai_riil * 0.36
        red_line_12 = nilai_riil * 0.12
        reward_3 = nilai_riil * 0.03

        print("\n" + "-"*60)
        print(f"1. TOTAL NILAI RIIL ASET   : Rp {nilai_riil:,.0f}")
        print(f"2. MARGIN DEPOSITO (36%)   : Rp {margin_36:,.0f}")
        print(f"3. BATAS KRITIS (12%)      : Rp {red_line_12:,.0f}")
        print(f"4. REWARD ADAB (3% WAJIB)  : Rp {reward_3:,.0f}")
        print("-" * 60)
        print("STATUS: OPERASIONAL - MEMBANGUN UNTUK ANAK CUCU")

    except ValueError:
        print("\n[!] Input Error: Gunakan angka nominal saja.")

    print("\n" + "="*60)
    print("        OTENTIK ICAM/SYAMS MAULANA - AL-HAQQ         ")
    print("="*60)

if __name__ == "__main__":
    main_protocol()
