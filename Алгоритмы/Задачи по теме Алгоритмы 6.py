'''
Закодируйте любую строку по алгоритму Хаффмана.
'''
import heapq
from collections import defaultdict

def build_huffman_tree(symbols_freq):
    heap = [[weight, [symbol, ""]] for symbol, weight in symbols_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    return heap[0]

def generate_huffman_codes(tree):
    huff_codes = {}
    for pair in tree[1:]:
        symbol, code = pair
        huff_codes[symbol] = code
    return huff_codes

def compress_data(text, huff_codes):
    compressed_data = ""
    for char in text:
        compressed_data += huff_codes[char]
    return compressed_data


def decompress_data(compressed_data, huff_codes):
    huff_codes_reversed = {code: symbol for symbol, code in huff_codes.items()}
    decoded_data = ""
    temp_code = ""

    for bit in compressed_data:
        temp_code += bit
        if temp_code in huff_codes_reversed:
            decoded_data += huff_codes_reversed[temp_code]
            temp_code = ""

    return decoded_data

text = "Закодируйте любую строку по алгоритму Хаффмана."

# Подсчет частоты символов в тексте
symbols_freq = defaultdict(int)
for symbol in text:
    symbols_freq[symbol] += 1

# Построение дерева Хаффмана и генерация кодов
huffman_tree = build_huffman_tree(symbols_freq)
huffman_codes = generate_huffman_codes(huffman_tree)

# Сжатие и распаковка данных
compressed_data = compress_data(text, huffman_codes)
decompressed_data = decompress_data(compressed_data, huffman_codes)

print(f"Исходный текст: {text}")
print(f"Сжатые данные: {compressed_data}")
print(f"Восстановленный текст: {decompressed_data}")

