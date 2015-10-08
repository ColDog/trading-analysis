def freq(words):
    fr = {}
    for word in words.split(' '):
        if fr.get(word):
            fr[word] += 1
        else:
            fr[word] = 1
    return fr
