# MR_PageRank

This is a simple Map Reduce implementation of page rank algorithm.

Dataset used for this implementation is from Google contest 2002 -> https://snap.stanford.edu/data/web-Google.html

The src folder contains 6 files 
- 2 mappers, 
- 2 reducers, 
- check_conv.py 
- iterate-hadoopp.sh. 

check_conv.py checks for convergence. While iterate-hadoop.sh is the script to automate the execution.

The data folder contains the sample data files. 

## Execution:

Please ensure proper permissions are given before executing the script. Command for that 
```chmod +x iterate-hadoop.sh```

```
bash iterate-hadoop.sh 
```
```
.\iterate-hadoop
```

