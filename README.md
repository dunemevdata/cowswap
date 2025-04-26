# CoWSwap Batch Statistics


## Data

The [data](./cowswap_batch.csv.zip) is from the anonymous Dune query: https://dune.com/queries/5028097, which contains all CoWSwap batches executed on Ethereum from January 2024 to January 2025. This dataset includes 808,096 batches and a total of 1,147,674 orders (each batch may contain multiple orders).

## Batch Statistics

Please install the dependencies using:

```shell
pip install networkx pandas
```

Then run the script with:
```shell
python3 count_cowswap_batch.py
```

The output will show the statistics:

```shell
Total batches: 808096
Total batches without cycles: 807212
Percentage of batches without cycles: 99.9%
70.7% of the batches have ≤ 2 tokens
77.5% of the batches have ≤ 3 tokens
92.9% of the batches have ≤ 4 tokens
95.9% of the batches have ≤ 5 tokens
98.5% of the batches have ≤ 6 tokens
99.3% of the batches have ≤ 7 tokens
99.7% of the batches have ≤ 8 tokens
99.9% of the batches have ≤ 9 tokens
```
