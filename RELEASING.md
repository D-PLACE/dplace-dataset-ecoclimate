# Releasing the ea


```shell
cldfbench makecldf cldfbench_ecoclimate.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench readme cldfbench_ecoclimate.py
cldfbench zenodo --communities dplace cldfbench_ecoclimate.py
dplace check cldfbench_ecoclimate.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_ecoclimate.py vX.Y
```