# Branching-system

## Merges

Merge "via mergerequest" means a merge-request on the source-control-management/project-server (like GitHub, GitLab, Azure DevOps, etc.).

Merge without the "via mergerequest"-attribute can either also be done via mergerequest and/or it can be done manually/using scripts. this depends on the project and must be defined by the product-owner.

Mergerequests in a code-management-tool are only required for merges to `stable`. When a mergerequest to `stable` will be created then all issues which are implemented on the mergerequest-source-branch must be linked. Mergerequests without having one (or more) linked issues are not allowed.
A mergerequest must not contain changes which are not related to any issue linked in the mergerequest.

## Branches and their meaning

The following branches will be used:

- `main` (contains the latest release, contains version-tags)
- `stable` (default-branch, contains version-tags)
- `feature/_issuenumber_`
- `bug/_issuenumber_`
- `codequality/_description_`
- `other/_description_`

For creating new features create a new branch from `stable` with the name `feature/_issuenumber_` and merge it back to `stable` via mergerequest.

For improving the code-quality create a new branch from `stable` with the name `codequality/_description_` and merge it back to `stable` via mergerequest.

For all changes which are not directly code-related (editing `ReadMe.md` or `License.txt` for example) create a new branch from `stable` with the name `other/_description_` and merge it back to `stable` via mergerequest.

For fixing bugs create a new branch from `main` with the name `bug/_issuenumber_` and merge it back to `main` if the bug is already on the `main`branch. If the bug is contained in the `stable`-branch but not on the `main`-branch then create a new branch from `stable` with the name `bug/_issuenumber_` and merge it back to `stable`. When a bug is contained neither on `main` nor on `stable` then fix the bug immediately on the branch where the bug occurs.

It is not allowed to commit on the `main`- and `stable`-branch directly. Changes on the branches are only allowed by a merge. Only the Branches `stable` and `bug/_issuenumber_` are allowed to get merged to `main`. A merge to `main` must always be a no-ff-merge.

Always when a merge to `main` will be done, then the following things must be done:

- Add a git-tag to the merge-commit containing the version-number.
- Run build-/release-pipeline.
- Optionally: Create a release of this version on the productive-system.
- When the source-branch of the merge was `bug/_issuenumber_` then merge `main` into `stable` without mergerequest. If possible, use a ff-merge.
- When the source-branch of the merge was `stable` then merge `main` back into `stable` using a ff-merge.

Always when a merge to `stable` will be done, then the following things must be done:

- Optionally: Run build-/release-pipeline.
- Add a git-tag to the merge-commit containing the version-number. (Only when it was not a ff-merge.)
- Optionally: Create a release of this version on the quality-management-system.

It is not allowed to commit or push on `main` or `stable` directly. Only exception: When a merge-commit was created without mergerequest then the merge-commit and the appropriate git-tag is allowed to get pushed.

## Branch-protection

The following recommendations for branch protections result from the description above:

| Branch | Allowed to merge         | Allowed to push | Allowed to force push  |
|--------|--------------------------|-----------------|------------------------|
| main   | Maintainers              | Maintainers     |           No           |
| stable | Developers + Maintainers | Maintainers     |           No           |
