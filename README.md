
## GRIP Benchmarking


Download data from the (https://github.com/kuzeko/graph-databases-testsuite/tree/V2) benchmark set
```
curl -O http://disi.unitn.it/~brugnara/data/GraphDatabaseComparison_BrugnaraLV_VLDBJ.tgz
```

Convert and load data
```
./convert.py dbpedia.escaped.json -o dbpedia
grip create dbpedia
grip load dbpedia --vertex dbpedia.vertex
grip load dbpedia --edge dbpedia.edge
```