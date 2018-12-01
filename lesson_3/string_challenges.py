# -*- coding: utf-8 -*-


# Вывести последнюю букву в слове
word = u'Архангельск'
print word[-1]

# Вывести количество букв а в слове
word = u'Архангельск'
print word.lower().count(u'а')

# Вывести количество гласных букв в слове
word = u'Архангельск'
vowels = u'аеуоэияюы'
print sum([1 for l in word if l in vowels])

# Вывести количество слов в предложении
sentence = u'Мы приехали в гости'
print len(sentence.split())

# Вывести первую букву каждого слова на отдельной строке
sentence = u'Мы приехали в гости'
print '\n'.join(w[0] for w in sentence.split())

# Вывести усреднённую длину слова.
sentence = u'Мы приехали в гости'
print len(sentence) / float(len(sentence.split()))
