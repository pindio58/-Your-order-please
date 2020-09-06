def order(sentence):
    container = []
    for num in range(len(sentence.split(' '))):
        container.append('')

    for name in sentence.split(' '):
        for num in name:
            if num.isdigit():
                container[int(num)-1] = name

    return ' '.join( char for char in container if char != '')
