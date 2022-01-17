# FreEM max OA

A Large Corpus for Early modern French - open access

For more information about FreEM corpora, cf. our [website](https://freem-corpora.github.io).

## Description

This repo contains documents of very different sources (wikipedia, scrapping, XML…).

* Documents gathered found online or given by colleagues are stored in the [0_source folder](https://github.com/FreEM-corpora/FreEMmax_OA/tree/master/0_source). Those given in a `.doc` / `.txt` format or found online are loosely encoded in TEI.
* New `teiHeader` are available with limited but highly structured information in the [1_header folder](https://github.com/FreEM-corpora/FreEMmax_OA/tree/master/1_header). These headers are used to generate the [table of content](https://github.com/FreEM-corpora/FreEMmax_OA/blob/master/TOC.tsv).
* It is possible to generate the final corpus with [`python3 build.py`](https://github.com/FreEM-corpora/FreEMmax_OA/blob/master/build.py). For legal reason, we are not allowed to modify files, so we provide the script to mofidy them. This script creates
1. a new version of the transcriptions with a minimal TEI encoding. They are adapted to [a dedicated ODD/schema](https://github.com/gabays/FreEMmax_OA/tree/master/ODD).
2. Cleaned `.txt` files

After execution of the script, we obtain the following data:

```
 |-0_source
  |-(.*).xml
  |-(.*).xml
  |-(.*).xml
  |- ...
 |-1_header
  |-(.*)_dAlembert.xml
  |-(.*)_dAlembert.xml
  |-(.*)_dAlembert.xml
  |- ...
 |-2_TEI
  |-(.*)_dAlembert.xml
  |-(.*)_dAlembert.xml
  |-(.*)_dAlembert.xml
  |- ...
 |-3_TXT
  |-(.*)_dAlembert.txt
  |-(.*)_dAlembert.txt
  |-(.*)_dAlembert.txt
  |-(.*)_dAlembert.txt
  |- ...
 |-ODD
   |-ODD_clean.ODD
   |-out
     |-ODD_clean.rng
 |-scripts
   |-build.xsl.xsl
   |-make_TOC.xsl
   |-1to2.xsl
```

## Table of content

A list of the files is available [here](https://github.com/FreEM-corpora/FreEMmax_OA/blob/master/TOC.tsv).

## Warning

This corpus is the open access version of the FreEM max corpus. Some (important) corpora are withdrawn from the available data.

## Licences
Cannot be distributed because of copyright reasons. Licences are given for each file. Some files should be removed, especially `EE_oldSpelling.xml` (_Electronic Enlightenment_ corpus, https://www.e-enlightenment.com/)

## Cite this repository
Simon Gabay, Alexandre Bartz, Philippe, Gambette, Alix Chagué, _FreEM max OA: A Large Corpus for Early modern French - Open access version_, Genève: Université de Genève, 2020, [https://github.com/FreEM-corpora/FreEMmax_OA](https://github.com/FreEM-corpora/FreEMmax_OA).

Please keep me posted if you use this data! simon.gabay[at]unige.ch

## Contact
simon.gabay[at]unige.ch
