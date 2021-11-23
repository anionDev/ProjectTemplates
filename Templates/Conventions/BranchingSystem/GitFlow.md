# Branching-system

Generally [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) will be used as branching-systm.

# Branches

There must be 2 branches: 

- `stable` (default-branch)
- `main` (contains version-tags)

Both branches are only allowed to get modified due to pull-requests or release-scripts.

When merging to stable (or immediately before) the build-pipeline should be executed.

When merging to main (or immediately before) the build-pipeline should be executed. Addtionally (when the build-pipeline ran without any issues) a git-tag (containing the version-number) on the merge-commit should be created and this version should be released.


## Branch-protection

The following recommendations for branch protections result from the description above:

| Branch | Allowed to merge         | Allowed to push | Allowed to force push  |
|--------|--------------------------|-----------------|------------------------|
| main   | Maintainers              | Maintainers     |           No           |
| stable | Developers               | Maintainers     |           No           |
