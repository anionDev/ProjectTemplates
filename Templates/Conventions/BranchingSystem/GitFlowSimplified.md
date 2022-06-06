# Branching-system

Generally [GitFlow](./GitFlow.md) will be applied as branching-system with the following modifications:

- There is no requirement for a `release`-branch when merging to the stable-branch. The `main`-branch can always be merged into the `stable`-branch if a release should be created. When the build-pipeline fails then the merge will be aborted and retried when the issue which caused the fail is resolved. If fixes in the source-code are required for that then the fixes must be implemented on a `bug`-branch and merged to the `main`-branch using the usual merge-process.
- When a merge to `stable` is completed then the merge back to the `main`-branch does not require executing the build-pipeline again and the merge-commit from `stable` back to `main` is allowed to be a no-ff-commit.
