# Branching-system

Generally [GitFlow](./GitFlow.md) will be applied as branching-systm with the following modifications:

- There is no requirement for a `release`-branch when merging to the stable-branch. The main-branch can always be merged into the stable-branch if a create should be created. When the build-pipeline fails then the merge will be aborted and retried when the issue which caused the fail is resolved.
- When a merge to `stable` is completed then the merge to the main-branch does not require executing the build-pipeline and it can be a ff-merge if possible.
