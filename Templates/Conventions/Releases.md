# Releases

There are to kinds of rules for repositories to differ:

- Reporitories which produce build-artefacts
- Reporitories which do not produce build-artefacts

## Rules for reporitories which produce build-artefacts

There must be something like a build-pipeline or (implemented using a pipeline in a source-control-management-server or a simple script) which is stored outside of the repository and which is doing all required steps automatically.

This pipeline must be executed when a merge-commit to the `main`-branch will be done.

## Rules for reporitories which do not produce build-artefacts

There must be something like a pipeline or script which is doing all required steps automatically.
