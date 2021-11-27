# Branching-system

Branches must be created from the `main`-branch and must always be merged back to this branch again using a merge-request or a script.

# Special branches

There must be 2 branches: 

- `main` (default-branch)

# Branch-protections

The following recommendations for branch protections result from the description above:

| Branch | Allowed to merge         | Allowed to push | Allowed to force push  |
|--------|--------------------------|-----------------|------------------------|
| main   | Maintainers              | Maintainers     |           No           |

# Hints

This branching-system is only applicable for repositories which do not produce build-artefacts and which also do not have build-pipeline.
