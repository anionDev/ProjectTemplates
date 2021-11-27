# Branching-system

Generally [GitFlow](https://nvie.com/posts/a-successful-git-branching-model/) will be applied as branching-systm.

# Special branches

There must be 2 branches: 

- `main` (default-branch)
- `stable`

# Branch-usage

Only stable-based bug-branches and the main-branch (using a temporary `release`-branch) are allowed to get merged to stable-branch. Merging to the stable-branch and to the main-branch is only allowed via Merge-request and as non-ff-commit.

When a merge to the `stable`-branch is completed then `stable` must be merged back to `main` due to a Merge-request.

When merging to `main` (or immediately before) the build-pipeline should be executed. The merge-request is not allowed to be completed when the build-pipeline fails.

When merging to `stable` (or immediately before) the build-pipeline should be executed. The merge-request is not allowed to be completed when the build-pipeline fails. Addtionally a git-tag (containing the version-number) on the merge-commit should be created and this version should be released.

# Branch-protections

The following recommendations for branch protections result from the description above:

| Branch | Allowed to merge         | Allowed to push | Allowed to force push  |
|--------|--------------------------|-----------------|------------------------|
| main   | Maintainers              | Maintainers     |           No           |
| stable | Developers               | Maintainers     |           No           |
