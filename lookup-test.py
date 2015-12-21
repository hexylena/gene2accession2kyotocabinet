#!/usr/bin/env python
from kyotocabinet import DB
import sys

# create the database object
db = DB()

# open the database
if not db.open("gene2accession.kch", DB.OWRITER | DB.OCREATE):
    print >>sys.stderr, "open error: " + str(db.error())

with open('gene2accession.min.tsv', 'r') as handle:
    for idx, line in enumerate(handle):
        if idx > 10:
            sys.exit()

        (prot_id, genome_id) = line.strip().split('\t')

        print '%10s => %10s' % (prot_id, db.get(prot_id))

if not db.close():
    print >>sys.stderr, "close error: " + str(db.error())
