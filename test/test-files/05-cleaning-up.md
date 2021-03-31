## Cleaning up

After committing the best experiment to Git, let's take another look at the
experiments table:

```
dvc exp show --no-timestamp \
             --include-params train.n_est \
             --no-pager
```{{execute}}

Where did all the experiments go? By default, `dvc exp show` only shows
experiments since the last commit, but don't worry. The experiments remain
cached and can be shown or applied. For example, use `-n` to show
experiments from the previous _n_ commits:

``` 
dvc exp show -n 2 --no-timestamp \
                  --include-params train.n_est \
                  --no-pager
```{{execute}}

Eventually, old experiments may clutter the experiments table.

`dvc exp gc` removes all references to old experiments:

``` 
dvc exp gc  --workspace 
dvc exp show -n 2 --no-timestamp \
                  --include-params train.n_est \ 
                  --no-pager
```{{execute}}

> [`dvc exp gc`][dvcexpgc] only removes references to the experiments, not the cached
> objects associated to them. To clean up the cache, use [`dvc gc`][dvcgc].

[dvcexpgc]: https://dvc.org/doc/command-reference/exp/gc
[dvcgc]: https://dvc.org/doc/command-reference/gc
