#!/bin/bash
# Convert pandoc markdown into Github flavoured markdown
pandoc -t gfm -o ../README.md  pdREADME.md
