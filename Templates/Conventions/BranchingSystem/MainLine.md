# Branching-system

The branching system applied in this repository is MainLine.

Branches must be created from the `main`-branch and must always be merged back to this branch. This merge-back can be done either by a merge-request or by a commit of a maintainer.
When merging to the `main`-branch it is recommended to create a git-tag including the version-number.

## Special branches

There must be the following branch:

- `main` (default-branch)

## Branch-protections

The following recommendations for branch protections result from the description above:

| Branch | Allowed to merge         | Allowed to push | Allowed to force push  |
|--------|--------------------------|-----------------|------------------------|
| main   | Maintainers              | Maintainers     |           No           |

## Hints

This branching-system is only applicable for repositories which do not produce build-artefacts and which also do not have build-pipeline.
