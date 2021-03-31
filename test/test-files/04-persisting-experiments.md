## Persisting experiments

Now that we know the best parameters, let's keep that experiment and
ignore the rest.

`dvc exp apply` rolls back the workspace to the specified experiment:

`dvc exp apply exp-2`{{execute}}

`dvc exp apply` is similar to [`dvc checkout`][dvccheckout], but it works with experiments. DVC
tracks everything in the pipeline for each experiment (parameters, metrics,
dependencies, and outputs) and can later retrieve it as needed.

Check that `scores.json` reflects the metrics in the table above:

`scores.json`{{open}}

Once an experiment has been applied to the workspace, it is no different from
reproducing the result without `dvc exp run`. Let's make it persistent in our
regular pipeline by committing it in our Git branch:

```
git add dvc.lock params.yaml prc.json roc.json scores.json
git commit -m "Preserve best Avg. Prec. experiment"
```{{execute}}

> [`dvc push`][dvcpush] only uploads persistent experiments that have been
> committed to Git. The other experiments will not be pushed to the remote. See
> [`dvc exp push`][dvcexppush] and [`dvc exp pull`][dvcexppull] for how to
> share other experiments.

[dvcpush]: https://dvc.org/doc/command-reference/push
[dvcexppush]: https://dvc.org/doc/command-reference/exp/push
[dvcexppull]: https://dvc.org/doc/command-reference/exp/pull
[dvccheckout]: https://dvc.org/doc/command-reference/checkout
