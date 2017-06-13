import re
import os
import sys
import time

import parse
import requests


def write_file(content, filename):
    # This assures that the 'books' directory exists, not part of the sheet.
    try:
        os.makedirs('books', 0o755)
    except OSError:
        pass

    with open(os.path.join('books', filename), 'w') as file_handle:
        file_handle.write(content)


def download(id):
    # Bonus task: measure time. Start time.
    download_time = time.time()

    res = requests.get('https://www.gutenberg.org/cache/epub/{id}/pg{id}.txt'
                       .format(id=id))

    # Bonus task: measure time. End time.
    download_time = time.time() - download_time
    return res.text, download_time


def save_book(text, author, title):
    write_file(text, '{}-{}.txt'.format(author, title))


def save_counts(words, counts, author, title):
    text = '\n'.join('{}, {}'.format(w, c) for w, c in zip(words, counts))
    write_file(text, '{}-{}-words.csv'.format(author, title))


def save_sentences(sentences, author, title):
    text = '\n\n'.join(sentences)
    write_file(text, '{}-{}-sentences.txt'.format(author, title))


def strip_book_meta(text, title):
    tpl = '*** {} OF THIS PROJECT GUTENBERG EBOOK {} ***'

    start = tpl.format('START', title.upper())
    end = tpl.format('END', title.upper())

    idx_start = text.index(start) + len(start)
    idx_end = text.index(end)

    book_content = text[idx_start:idx_end]

    return book_content


def get_words(filename='wordlist.txt'):
    with open(filename) as file_handle:
        return file_handle.read().splitlines()


def find_sentences(content):
    words = get_words()
    counts = []
    sentences = []

    for word in words:
        results = re.findall(r'[^.!?]*\b{}\b[^.!?]*[.!?]'.format(word),
                             content, re.DOTALL | re.IGNORECASE)
        if results:
            counts.append(len(results))
            sentences.append(results[0])
        else:
            counts.append(0)
            sentences.append('')

    return words, counts, sentences


def get_meta(text):
    pgline = text.splitlines()[0]
    result = parse.parse(
        '\ufeffThe Project Gutenberg EBook of {title}, by {author}',
        pgline)
    return result['author'], result['title']


def print_info(id, author, title, download_time, words, counts, sentences):
    print('Downloaded {}, {}: {}, in {:.3f} s.'.format(id, author, title,
                                                       download_time))
    print('\nThe word counts are:')
    for word, count in zip(words, counts):
        print('  {: <8}{: >4}'.format(word, count))

    print('\nSome example sentences:\n')
    count = 0
    for sentence in sentences:
        if sentence:
            count += 1
            print(sentence + '\n')
        if count >= 2:
            break


def main():
    # Bonus task: Read ID from command line arguments.
    pgid = sys.argv[1]
    full_text, download_time = download(pgid)

    author, title = get_meta(full_text)

    book_content = strip_book_meta(full_text, title)

    words, counts, sentences = find_sentences(book_content)

    save_book(full_text, author, title)
    save_counts(words, counts, author, title)
    save_sentences(sentences, author, title)

    print_info(pgid, author, title, download_time, words, counts, sentences)


if __name__ == '__main__':
    main()
