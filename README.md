# gene2accession2kyotocabinet

This repository contains a simple makefile and python script for converting
NCBI's gene2accession table into an extremely fast kyotoCabinet database for
searching

## Examples

```console
$ make

# This step takes a long time. First it extracts the protein + genome GIs into
# the gene2accession.min.tsv file. Then they're converted into a kyoto-cabinet
# database (gene2accession.kch)

$ du -h gene2accession.*
845M    gene2accession.kch
517M    gene2accession.min.tsv
4.8G    gene2accession.tsv

# At the end, our database is lightning fast:

$ (env)user@host: time python lookup-test.py
  3282737 =>    3282736
 10954455 =>   10954454
  3282739 =>    3282736
 10954457 =>   10954454
  3282740 =>    3282736
219730360 =>  219730359
219783138 =>  219783137
257293830 =>  257293829
257287470 =>  257287469
 10954458 =>   10954454
  3282741 =>    3282736

real    0m0.015s
user    0m0.010s
sys     0m0.005s
```
