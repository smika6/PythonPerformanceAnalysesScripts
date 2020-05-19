Created by Jacob Hopkins
Shared 5/19/2020
This file was made to compare the performance of generators to lists, using fibonacci numbers. 
This also compares using iterative and recursive methods, even memoised recursion.

Run the file by sending it to the python interpreter.

Sample output
==============================================================================================
Terms to generate: 10000


Recursive & Generator
Memory (Before): [121.92578125] Mb
Memory (After): [121.92578125] Mb
Memory (Difference): 0.0 Mb
Time to create 10000 numbers: 0.20004487037658691 Seconds
Time to add 10000 numbers: 0.013002634048461914 Seconds
Time to create and add 10000 numbers: 0.21304750442504883 Seconds


Recursive & List
Memory (Before): [121.92578125] Mb
Memory (After): [125.44921875] Mb
Memory (Difference): 3.5234375 Mb
Time to create 10000 numbers: 0.21303272247314453 Seconds
Time to add 10000 numbers: 0.002000093460083008 Seconds
Time to create and add 10000 numbers: 0.21503281593322754 Seconds


Recursive w/ Memoise & Generator
Memory (Before): [120.6484375] Mb
Memory (After): [120.6484375] Mb
Memory (Difference): 0.0 Mb
Time to create 10000 numbers: 0.20004773139953613 Seconds
Time to add 10000 numbers: 0.008002281188964844 Seconds
Time to create and add 10000 numbers: 0.20805001258850098 Seconds


Recursive w/ Memoise & List
Memory (Before): [120.6484375] Mb
Memory (After): [122.8515625] Mb
Memory (Difference): 2.203125 Mb
Time to create 10000 numbers: 0.20781469345092773 Seconds
Time to add 10000 numbers: 0.0020029544830322266 Seconds
Time to create and add 10000 numbers: 0.20981764793395996 Seconds


Iterative list
Memory (Before): [122.1328125] Mb
Memory (After): [123.4765625] Mb
Memory (Difference): 1.34375 Mb
Time to create 10000 numbers: 0.20304512977600098 Seconds
Time to add 10000 numbers: 0.0010008811950683594 Seconds
Time to create and add 10000 numbers: 0.20404601097106934 Seconds


Iterative each value w/ List
Memory (Before): [122.4765625] Mb
Memory (After): [123.82421875] Mb
Memory (Difference): 1.34765625 Mb
Time to create 10000 numbers: 6.6794493198394775 Seconds
Time to add 10000 numbers: 0.002001047134399414 Seconds
Time to create and add 10000 numbers: 6.681450366973877 Seconds


Iterative each value w/ Generator
Memory (Before): [122.82421875] Mb
Memory (After): [122.82421875] Mb
Memory (Difference): 0.0 Mb
Time to create 10000 numbers: 0.20004487037658691 Seconds
Time to add 10000 numbers: 6.490558624267578 Seconds
Time to create and add 10000 numbers: 6.690603494644165 Seconds
=======================================================================================
Conclusion:

Iterative creation directly into a stored list was the fastest: 0.20404601097106934 Seconds, 1.34375 Mb

Memoised Recursive was the second fastest: 0.20805001258850098 Seconds & 0.20981764793395996 Seconds
and the generator of such had the best memory performance of 0mb
while the list version of memoised was memory heavy: 2.203125 Mb

I would the iterative list creating function, for the memoised one creates a cache in ram that is unneccisary in this application.
Also it is fastest, and has a small memory footprint. 
