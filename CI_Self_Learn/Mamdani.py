respon_time = 2 # menit (Cepat, Sedang, Lambat)
clarity = 7 # (rentang 0-10) (Sangat Jelas, Kurang Jelas, Tidak Jelas)

# Oke sekarang kita define dulu batas cutt off masing-masing nilai
'''
Untuk respon time :
1. Jika dia respon < 2 menit (cepat)
2. 2-7 menit (sedang)
3. > 7 menit (lambat)

Untuk clarity :
1. Clarity = 10 (sangat jelas)
2. Clarity dari 4-9 (kurang jelas)
3. Clarity <= 3 (Tidak Jelas)
'''

def membership_function(respon_time, a, b, c):
    """
    Kita akan memakai jenis fungsi segitiga
    Sekarang kita akan buat batasan setiap jenis fuzzy untuk respon time (Pakai rentangan kontinu dari 0 - 1)
    1.Batas Minimum 1 menit

    """
    if respon_time <= a or respon_time >= c:
        return 0
    
    
    return

