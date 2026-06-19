import os

WATERMARK_TEXT = """

---
> **Cap Digital Kolaborasi Pemikiran Terverifikasi**
> Identitas Otentik: ICAM / Syams Maulana
> Framework: Inverted Pyramid v1.6 | Aliansi Al-Haqq
"""

def inject_watermark():
    for root, dirs, files in os.walk("."):
        if ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                
                if "ICAM / Syams Maulana" not in content:
                    print(f"[+] Menanamkan watermark pada: {file_path}")
                    with open(file_path, "a", encoding="utf-8") as f:
                        f.write(WATERMARK_TEXT)
                else:
                    print(f"[-] Sudah aman (terverifikasi): {file_path}")

if __name__ == "__main__":
    inject_watermark()
