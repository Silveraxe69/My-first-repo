def add_prefix_un(word):
    return 'un' + word


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    prefixed_words = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + prefixed_words)


def remove_suffix_ness(word):
    if word.endswith('iness'):
        return word[:-4].replace('i', 'y')
    return word[:-4]


def adjective_to_verb(sentence, index):
    words = sentence.split()
    adjective = words[index].rstrip('.')
    if adjective.endswith('ic'):
        return adjective[:-2] + 'ize'
    elif adjective.endswith('al'):
        return adjective[:-2] + 'ate'
    else:
        return adjective + 'en'
