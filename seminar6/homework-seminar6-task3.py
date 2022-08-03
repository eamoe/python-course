# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Get data from a file
from fileinput import close


def get_data_from_file(path):
    file = open(path, 'r')
    line = file.readline()
    file.close()
    return line

# Write data to a file
def write_data_to_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

# Split a string to substrings
def get_substrings(line):
    output_str = ""
    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            output_str += line[i]
        else:
            output_str += line[i] + ";"
    output_str += line[len(line) - 1]
    return output_str.split(";")

# Compress string with RLE algorithm
def string_compressor(line):
    substrings = get_substrings(line)
    symbol_count_list = [element[0] + str(len(element)) for element in substrings]
    compressed_str = ""
    for element in symbol_count_list:
        compressed_str += element
    return compressed_str
    

def string_decompressor(line):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(line) - 1):
        symbol = line[i]
        count = int(line[i + 1])
        for j in range(count):
            decoded_message = decoded_message + symbol
            j = j + 1
        i = i + 2
    return decoded_message


#Main program
file_path = 'file_to_compress.txt'
data_to_compress = get_data_from_file(file_path)
print(f"Данные для сжатия: {data_to_compress}")

compressed_data = string_compressor(data_to_compress)
write_data_to_file("compressed_file.txt", compressed_data)
print(f"Результат сжатия: {compressed_data}\n")

file_to_decompress = 'compressed_file.txt'
data_to_decompress = get_data_from_file(file_to_decompress)
print(f"Данные в сжатом файле: {data_to_decompress}")
print(f"Распакованные данные: {string_decompressor(data_to_decompress)}")