data_kelembapan = [22, 28, 34, 41, 55, 63, 72, 78, 31, 47, 66, 81, 19, 58, 69, 10, 90, 50, 77, 5] 

def status_sensor(nilai):
    if  nilai < 35:
        return "KERING" 
    elif nilai  <= 70:
        return "NORMAL" 
    else:
        return "BASAH"

def aksi_pompa(status):
    if status == "KERING":
        return "POMPA ON"
    else:
        return "POMPA OFF"

def rata_rata(data):
    total = 0 
    for nilai in data:
        total += nilai
    return total / len(data)

def hitung_kategori(data):
    kering = 0
    normal = 0
    basah = 0
    for nilai in data:
        status = status_sensor(nilai)
        if status == "KERING":
            kering  += 1
        elif status == "NORMAL":
            normal += 1
        else:
            basah += 1
    return kering, normal, basah

print("---Monitoring Kelembapan Tanah & Aksi Pompa---")

for i in range(len(data_kelembapan)):
    nilai = data_kelembapan[i]
    status = status_sensor(nilai)
    pompa = aksi_pompa(status)
    print(i+1, ".", nilai, "%", "=", status, "->", pompa)

kering, normal, basah = hitung_kategori(data_kelembapan)

print("=== RINGKASAN  ===")
print("Total Data :", len(data_kelembapan))
print("Total KERING :", kering)
print("Total NORMAL :", normal)
print("Total BASAH :", basah)
print("Rata-rata :", rata_rata(data_kelembapan), "%")
print("Nilai maksimum :", max(data_kelembapan), "%")
print("Nilai minimum :", min(data_kelembapan), "%")














