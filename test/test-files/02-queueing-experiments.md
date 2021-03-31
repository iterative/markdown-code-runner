## Queueing experiments

We have been tuning the `featurize` stage so far, but there are also parameters
for the `train` stage, which trains a [random forest classifier][rfc].

[rfc]: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html

`params.yaml`{{open}}

Let's setup experiments with different hyperparameters. We can define all the
combinations we want to try without executing anything, by using the `--queue`
flag:

```
dvc exp run --queue -n exp-1 -S train.n_est=50
dvc exp run --queue -n exp-2 -S train.n_est=100
dvc exp run --queue -n exp-3 -S train.n_est=150
dvc exp run --queue -n exp-4 -S train.n_est=200
```{{execute}}

The `-n` option is used to label the experiments. If it's not specified,
DVC provides a name. We set the names for easier reference here. 

Next, run all queued experiments using `--run-all`:

`dvc exp run --run-all`{{execute}}

