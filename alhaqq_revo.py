import sys
import time

def jalankan_protokol():
    # --- KONSTRUKSI VARIABEL 92% (NON-NEGOTIABLE) ---
    PERSEN_MARGIN_AWAL = 0.36
    AMBANG_BATAS_KRITIS = 0.12
    REWARD_KOOPERATIF = 0.03
    
    print("\n" + "="*50)
    print("      AL-HAQQ ABSOLUTE REVO PROTOCOL (ICAM_K1.6)      ")
    print("      INTEGRATED WITH TIS ECOSYSTEM - VER 0.92      ")
    print("="*50)
    print("[*] Status: Encrypted & Real-Time Sync Ready")
    time.sleep(1)

    try:
        # Input Nilai Riil (SNA - Satuan Nilai Aset)
        harga_aset = float(input("\n[>] Masukkan Nilai Riil Aset (Kurs Real-Time): "))
        
        # Kalkulasi Al-Haqq
        deposit_36 = harga_aset * PERSEN_MARGIN_AWAL
        limit_12 = harga_aset * AMBANG_BATAS_KRITIS
        reward_3 = harga_aset * REWARD_KOOPERATIF
        management_bank = (harga_aset * 0.12) - reward_3 # Bank ambil 9% net di titik kritis

        print("\n" + "-"*50)
        print(f"1. TOTAL NILAI ASET        : Rp {harga_aset:,.2f}")
        print(f"2. MARGIN DEPOSITO (36%)   : Rp {deposit_36:,.2f} (FILTER NASIB)")
        print(f"3. RED LINE MUFAKAT (12%)  : Rp {limit_12:,.2f} (LIMIT RISIKO)")
        print(f"4. DIGNITY REWARD (3%)     : Rp {reward_3:,.2f} (Wajib dibayar Bank)")
        print("-"*50)

        print("\n[ANALISIS RASIONALITAS]")
        if deposit_36 > 0:
            print(f"> Pesan: Jika ingin menikah/ambil aset, pastikan Rp {deposit_36:,.2f} siap.")
            print("> Status: Menekan Nafsu, Mengutamakan Akal Sehat.")

        print("\n[KETENTUAN FINAL 92%]")
        print("- Bunga/Interest: 0% (CLEAN)")
        print("- Asuransi: 0% (Internal Collaboration Protection)")
        print("- Exit Clause: Jika Margin < 12%, Mufakat Aktif.")
        print("- Bank Integrity: Wajib transfer 3% kompensasi ke Nasabah.")

    except ValueError:
        print("\n[!] Error: Masukkan angka yang valid.")

    print("\n" + "="*50)
    print("       OTENTIK ICAM/SYAMS MAULANA - AL-HAQQ       ")
    print("="*50)

if __name__ == "__main__":
    jalankan_protokol()
