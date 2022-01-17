#!/usr/bin/env bash

java -jar scripts/saxon-he-10.3.jar -o:TOC.tsv  scripts/make_TOC.xsl scripts/make_TOC.xsl
