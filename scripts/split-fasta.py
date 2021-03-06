#! /usr/bin/env python
import sys
from screed.fasta import fasta_iter

filename = sys.argv[1]
prefix = sys.argv[2]
size = int(float(sys.argv[3]))          # e.g. 1e9

division = -1
for n, record in enumerate(fasta_iter(open(filename), parse_description=False)):
    if n % 100000 == 0:
        print '...', n
        
    if n % size == 0:
        division += 1
        new_name = '%s.%04d.fa' % (prefix, division)
        print 'opening', new_name
        fp = open(new_name, 'w')

    fp.write('>%s\n%s\n' % (record['name'], record['sequence']))
