word = 'testing'
print(word[len(word) // 2] if len(word) % 2 != 0 else word[len(word) // 2 - 1] + word[len(word) // 2])
