# Branching-system

The branching system applied in this repository is GitFlow.

Generally [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) will be applied as branching-system.

## branch-names

There must always be 2 special branches:

- `main` (default-branch)
- `stable`

All other branches must have a name matching one of the following name-patterns:

- `^bug\/\S+`
- `^codequality\/\S+`
- `^feature\/\S+`
- `^other\/\S+`
- `^release\/\S+`

## Branch-usage

Only `stable`-based `bug`-branches and the `main`-branch (using a temporary `release`-branch) are allowed to get merged to `stable`-branch. Merging to the `stable`-branch and to the `main`-branch is only allowed via merge-request and as non-ff-commit.

When merging a `release`-branch to the `stable`-branch is completed then `stable` must be merged back to `main` due to another merge-request.

When merging to `main` or `stable` (or immediately before) the build-pipeline must be executed. The merge-request is not allowed to be completed when the build-pipeline or any other related scripts/tasks/validations fail.

Additionally, when merging to `main` a git-tag (containing the version-number) on the merge-commit must be created.

When merging to `stable` then the build-artifact created by the build-pipeline immediately before is supposed to be released.

## Branch-protections

The following recommendations for branch protections result from the description above:

| Branch   | Allowed to merge         | Allowed to push | Allowed to force push  |
|----------|--------------------------|-----------------|------------------------|
| `main`   | Maintainers              | Maintainers     |           No           |
| `stable` | Maintainers              | Maintainers     |           No           |

## Hints

### Wording

#### Build-pipeline

Typically "build-pipeline" means an automated "classical" pipeline executed by the collaboration-server and its build-server (e. g. GitLab or Azure DevOps) but using build-scripts are also acceptable in the sense of this `GitFLow`-definition.
