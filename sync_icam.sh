#!/bin/bash
echo "Mengunci Metadata Al-Haqq..."
# Update status ke 100%
yq -i '.identifier.value = "ICAM_K1.6_COMPLETE"' identity.jsonld

echo "Menanamkan Watermark Digital..."
for file in *.txt; do
    [ -e "$file" ] || continue
    echo -e "\n---\nOtentik ICAM/Syams Maulana\nAl-Haqq Compliance" >> "$file"
done

echo "Push ke Repositori Utama..."
git add .
git commit -m "Deployment: Matrix Sync 100% (Tidore Prep)"
git push origin main

echo "All systems are GO. Alhamdulillah."
