import struct
packed = struct.pack('>i4sh' , 7, b'spam',8)
print(packed)
file = open('data.bin', 'wb') # Открыть двоичный файл для записи
print(file .write(packed))
file.close()
