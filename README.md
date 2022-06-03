# 022-apriori-algorithm

022 apriori algorithm

Basic big data algorithm, using apriori algorithm to measure related data.

## input.txt

1 2 3

1 2 3 4

2 3 5

1 3 4 5

4 5

## output.txt

1 1 3

1 2 3

1 3 4

1 4 3

1 5 3

2 1 2 2

2 1 3 3

2 1 4 2

2 2 3 3

2 3 4 2

2 3 5 2

2 4 5 2

3 1 2 3 2

3 1 3 4 2

## output in cmd

Lines in database is: 5

minSupport: 2

itemset read completed.

Calculating ...

(1.0) ----------> 3.0

(2.0) ----------> 3.0

(3.0) ----------> 4.0

(4.0) ----------> 3.0

(5.0) ----------> 3.0

(1.0, 2.0) ----------> 2.0

(1.0, 3.0) ----------> 3.0

(1.0, 4.0) ----------> 2.0

(2.0, 3.0) ----------> 3.0

(3.0, 4.0) ----------> 2.0

(3.0, 5.0) ----------> 2.0

(4.0, 5.0) ----------> 2.0

(1.0, 2.0, 3.0) ----------> 2.0

(1.0, 3.0, 4.0) ----------> 2.0
