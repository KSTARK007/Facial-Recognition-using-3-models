echo getting data
rm -rf .\data\* 
googleimagesdownload --keywords "keanureevesjohnwick" --limit 50 -o "data" -f "jpg"
face_recognition --cpus -1 .\data\keanureevesjohnwick\ .\extractedframes\ >out.txt
pause