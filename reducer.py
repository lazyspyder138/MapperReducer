#!/usr/bin/python
import sys
import bisect
index = {}

for line in sys.stdin:
    word, postings = line.split('\t')
    index.setdefault(word, {})
    for posting in postings.split(','):
        doc_id, loc = posting.split(':')
        loc = int(loc)
        index[word].setdefault(doc_id, [])
        bisect.insort(index[word][doc_id],loc)
        #index[word][doc_id].append(loc)
for word in index:
    postings_list = ["%s:%s" % (doc_id, index[word][doc_id]) for doc_id in index[word]]
    postings = ','.join(postings_list)
    print('%s\t%s' % (word, postings))
