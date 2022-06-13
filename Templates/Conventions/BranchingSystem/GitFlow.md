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

Only the `main`-branch (using a temporary `release`-branch) are allowed to get merged to `stable`-branch. It is not allowed to merge the same version to the `stable`-branch twice. Merging to the `stable`-branch and to the `main`-branch is only allowed via merge-request and as non-ff-commit.

When merging a `release`-branch to the `stable`-branch is completed and there were commits done on the `release`-branch then `stable` must be merged back to `main` as soon as possible due to another merge-request which results in a non-ff-mergecommit.
After that the version of the main-branch must be incremented/tagged accordingly.

When merging to `main` or `stable` (or immediately before) the build-pipeline must be executed. The merge-request is not allowed to be completed when the build-pipeline or any other related scripts/tasks/validations fail.

Additionally, when merging to `main` a git-tag (containing the version-number) on the merge-commit must be created.

When merging to `stable` then the build-artifact created by the build-pipeline immediately before is supposed to be released.
When merging to `stable` then the merge-commit is not allowed to be git-tagged.
The reason for that is that the commit on a `stable`-branch is treated as release.
And a release (in this sense) is based on a version which is already defined by the latest `main`-branch's version which is contained in the `stable`-branch.
There may be commits "between" the `main`- and the `stable`-branch if (and only if) commits will be done on the `release`-branch in the context of the merge-request from `main` to `stable`.
But this is no problem because the release-version (and consequently the version of the `stable`-branch) is still unique because there can not be another release from the same `main`-branch-version.

## Branch-protections

The following recommendations for branch protections result from the description above:

| Branch   | Allowed to merge         | Allowed to push | Allowed to force push  |
|----------|--------------------------|-----------------|------------------------|
| `main`   | Maintainers              | Maintainers     |           No           |
| `stable` | Maintainers              | Maintainers     |           No           |

## Hints

### Wording

#### Build-pipeline

Typically "build-pipeline" means an automated "classical" pipeline executed by the collaboration-server and its build-server (e. g. [GitLab](https://gitlab.com/) or [Azure DevOps Server](https://azure.microsoft.com/en-us/services/devops/server)) but using build-scripts are also fine in the sense of this `GitFLow`-definition.
