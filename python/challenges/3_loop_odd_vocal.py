# TODO: Program untuk mencetak bilangan ganjil dari 1 hingga 15
odd_numbers = [x for x in range(1, 16) if x % 2 == 1]
print(odd_numbers)

# TODO: Program menghitung jumlah huruf vokal
word = input("Masukkan kata: ").lower()

vowels = "aiueo"
count = sum(1 for x in word if x in vowels)

print("Jumlah huruf vokal:", count)
