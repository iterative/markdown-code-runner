## Comparing many experiments

To compare all of these experiments, we need more than `dvc exp diff`: 

`dvc exp show` compares any number of experiments in one table:

```
dvc exp show --no-timestamp \
             --include-params train.n_est \
             --no-pager
```{{execute}}

Although the differences in metrics are minuscule due to the small size of
the data set, `exp-2` is a bit better in terms of `avg_prec`.
