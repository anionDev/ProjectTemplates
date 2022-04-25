# CommonProjectStructure

## Requirements

The repository must implement the requirements defined by [MinimalRequirements](./MinimalRequirements.md).

The `ReadMe.md`-file must contain a runtime-dependency-list and a development-dependency-list for the project.

Furthermore the repository must contain the following file with appropriate content:

- [`GitVersion.yml`](https://github.com/GitTools/GitVersion)
- [`<projectname>.code-workspace`](https://code.visualstudio.com/docs/editor/workspaces)

If the source-code of the project is publicly available then also the following file must be contained:

- [`.well-known/security.txt`](https://securitytxt.org/)

A project an contain multiple (but at least one) code-units.
A code-unit is a compilable part of the project. Small projects may often have only one code-unit. A typical 3-tier-web-application which processes data for example will probably have 3 code-units (e. g. for web-part, backend-part and database-part).
Testcases for a code-unit are part of the code-unit and are not a further code-unit.
For each code-unit the repository must contain the following files and folder with appropriate content:

- `<codeunit>/Other/QualityCheck/RunTestcases.py`
- `<codeunit>/Other/QualityCheck/Linting.py`
- `<codeunit>/Other/QualityCheck/TestCoverage/TestCoverage.xml`
- `<codeunit>/Other/QualityCheck/TestCoverage/TestCoverageReport`
- `<codeunit>/Other/Reference/GenerateReference.py`
- `<codeunit>/Other/Reference/ReferenceContent`
- `<codeunit>/Other/Reference/GeneratedReference`
- `<codeunit>/Other/Build/Build.py`
- `<codeunit>/Other/Build/BuildArtifact`
- `<codeunit>/<codeunit>`
- `<codeunit>/<codeunit>.codeunit`
- `<codeunit>/<codeunit>Tests`

A merge on the main-branch is only allowed if the scripts `RunTestcases.py`, `Linting.py`, `GenerateReference` and `Build.py` exits with 0 for each code-unit.
At the latest when the merge-commit will be done then the following things must be done for each code-unit which has been changed in the merge:

- The `TestCoverage.xml`-file must be updated by running `RunTestcases.py`.
- The version in the `<codeunit>.codeunit`-file must be changed to a higher version.

## Further explanations

### `RunTestcases.py`

It is expected that the file `RunTestcases.py` is a python3-script which exits with a non-zero-exitcode if at least one testcase fails. This script does not have to consider the minimum test-coverage defined by `<codeunit>.codeunit` because this is a task of a release-script.

If something like compiling is required to run the testcases then this script must do that. These compiled files may not be placed in any not git-ignored-folder.

This script should generate or update `TestCoverage.xml` and `TestCoverageReport`.

### `TestCoverage.xml`

It is expected that `TestCoverage.xml` contains a test-coverage-report of the code-unit in the cobertura-format.

### `TestCoverageReport`

It is expected that after running `RunTestcases.py` the folder `TestCoverageReport` contains a `index.html` containing a html-report about the unittest-coverage based on `TestCoverage.xml`.
The `TestCoverageReport`-folder does not have to be committed.

### `Linting.py`

It is expected that the file `Linting.py` is a python3-script which exits with a non-zero-exitcode if there is at least one linting-issue.

### `GenerateReference.py`

It is expected that the file `GenerateReference.py` is a python3-script which generates or updates the reference in `GeneratedReference` and exits with a non-zero-exitcode if at least one error occurs.

### `ReferenceContent`

The folder `ReferenceContent` must contain a reference for the code-unit. The content of this folder is the source of the `GeneratedReference`-folder.
The `ReferenceContent`-folder must be committed.

### `GeneratedReference`

It is expected that after running `GenerateReference.py` the folder `GeneratedReference` contains an `index.html`-file containing a html-reference about the code-unit on `ReferenceContent`.
The `GeneratedReference`-folder does not have to be committed.

### `Build.py`

It is expected that the file `Build.py` is a python3-script which creates the build-artefact of the code-unit for productive usage and exits with a non-zero-exitcode if the build fails for any reason.
The build-artefact should be placed in `BuildArtifact`.

### `BuildArtifact`

It is expected that the folder `BuildArtifact` is git-ignored.

### `<codeunit>`

It is expected that the folder `<codeunit>/<codeunit>` contains the source-code of the code-unit.

### `<codeunit>.codeunit`

It is expected that the folder `<codeunit>` contains the file `<codeunit>.codeunit` with the following xml-content.

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<codeunit:codeunit codeunitspecificationversion="1.0.0" xmlns:codeunit="https://github.com/anionDev/ProjectTemplates" xmlns:schemaLocation="https://raw.githubusercontent.com/anionDev/ProjectTemplates/main/Templates/Conventions/RepositoryStructure/codeunit.xsd">
    <codeunit:name>codeunit</codeunit:name>
    <codeunit:version>1.0.0</codeunit:version>
    <codeunit:minimalcodecoverageinpercent>90</codeunit:minimalcodecoverageinpercent>
</codeunit:codeunit>
```

The values inside the xml-document must obviously be adapted.

While the project-version-specification is defined by [MinimalRequirements](./MinimalRequirements.md) a code-unit-version is independent of the project version but the rules to change code-unit-versions are the same as the rules for changing the project-version. So a code-unit-version can always be the same as the project-version but it does not have to.

### `<codeunit>/<codeunit>Tests`

It is expected that the folder `<codeunit>/<codeunit>Tests` contains the unit-tests of the code-unit.
