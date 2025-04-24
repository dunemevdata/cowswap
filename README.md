# CowSwap Batch Statistics


## Data

The [data](./cowswap_batch.csv.zip) is from the anonymous Dune query: https://dune.com/queries/5028097, which contains all executed batches through CoWSwap from January 2024 to January 2025. This dataset includes 808,096 batches and a total of 1,147,674 orders, as some batches contain multiple orders.

## Batch Statistics

Please install the dependencies using:

```shell
pip install networkx pandas
```

Then run the script with:
```shell
python3 count_cowswap_batch.py
```

The output will show basic statistics:

```shell
Total batches: 808096
Total batches without cycles: 807212
Percentage of batches without cycles: 99.9%
```
