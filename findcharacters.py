

word_list = ['hello','world','my','name','is','Anna']
char = 'l'
new_word_list = []

for word in word_list:
    if char in word:
        new_word_list.append(word)
print new_word_list