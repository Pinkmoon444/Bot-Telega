# Ошибка - исключение - Exception
# Возникает в случае недопустимых действий (например, при выходе за пределы индекса или при делении на ноль)

# Ошибка останавливает воспроизведение кода

# Ошибки можно поймать и продолжить воспроизводить код

try:
    x = 1/0
except:
    print('Ошибку поймали!')
print('Всё хорошо! Код добрался до этой строчки')

# в блок try убираем строки, которые могут вызвать ошибки. Код внутри этого блока выполняется всегда.

# Если внутри блока try произошла ошибка, то выполняется содержимое блока except