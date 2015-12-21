#!/usr/bin/env python
from kyotocabinet import DB
import sys

# create the database object
db = DB()

# open the database
if not db.open("gene2accession.kch", DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())


with open('gene2accession.min.tsv', 'r') as handle:
    for line in handle:
        (prot_id, genome_id) = line.strip().split('\t')
        if prot_id == '-' or genome_id == '-':
            continue

        if not db.set(prot_id, genome_id):
            print >>sys.stderr, "set error: " + str(db.error())

if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())
