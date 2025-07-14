# Membuat pengecekan password
# Ketika yang diinput kurang dari 7 karakter -> "Karakter kurang"
# Ketika yang diinput sama atau lebih dari 7 karakter -> "Karakter cukup"

# Input password
password = input("Masukkan password: ")

# Pengecekan password 
if len(password) < 7:
    print("Karakter kurang")
else:
    print("Karakter cukup")
# Input password
password = input("Masukkan password: ")

# Pengecekan password 
if len(password) < 8:
    print("Karakter kurang")
else:
    print("Karakter cukup")
