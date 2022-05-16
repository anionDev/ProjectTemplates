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
- `<codeunit>/Other/PrepareMerge.py`
- `<codeunit>/Other/Build/Build.py`
- `<codeunit>/Other/Build/BuildArtifact`
- `<codeunit>/<codeunit>.codeunit`

`<codeunit>` must be replaced by the name of the code-unit which must be in [Pascal-case](https://www.theserverside.com/definition/Pascal-case).
A merge on the main-branch is only allowed if the scripts `PrepareMerge.py`, `RunTestcases.py`, `Linting.py`, `GenerateReference`exits with 0 for each code-unit. It is also recommended to run `Build.py` to ensure that the build-script also runs without any errors.

The project's version is defined by the output of `gitversion /showVariable MajorMinorPatch`.

## Further explanations

### `<codeunit>`

It is expected that the folder `<codeunit>` contains the source-code of the code-unit including its testcases and (if available) the ui-translations of the project (e. g. `.arb`-files or `.xlf`-files).

If the used programming language provides a specific sourcecode-structure recommended by the maintainer of the programming-language then it is recommended to follow these conventions. This recommendation still applies even the recommendations are contrary to the other regulations described here. The purpose of this is that some programming languages enforce a more or less strictly defined structure. It is often advisable to follow them and sometimes nearly impossible to not follow them. But it is definitely impossible in practice to find two programming languages or frameworks which have exactly the same project-structure, style-guide, etcetera.
The aim of the common project structure is to be flexible and usable for many programming languages and frameworks, no matter what their requirements and recommendations say.Style-mixtures are inevitable when you use different programming languages for frontend and backend (and this is often the case). And this is absolutely fine because on the one hand this is normal and no problem in practice. And on the other hand code-units should be independent and there is no requirement to adjust the structure and style of a code-unit to another not recommended structure and style.

### `PrepareMerge.py`

It is expected that the file `PrepareMerge.py` is a python3-script which exits with a non-zero-exitcode if  it fails.
This script is supposed to do things like update the version in `<codeunit>.codeunit` or other files of the code-unit.

If the version of the code-unit should follow the project's version to always be the same, then `PrepareMerge.py` must update the version in `<codeunit>.codeunit` (and also in other files of this code-unit if desired).

### `RunTestcases.py`

It is expected that the file `RunTestcases.py` is a python3-script which exits with a non-zero-exitcode if at least one testcase fails. This script does not have to consider the minimum test-coverage defined by `<codeunit>.codeunit` because this is a task of a merge-script.

If something like compiling is required to run the testcases then this script must also do that. These compiled files may not be placed in any not git-ignored-folder.

This script must generate or update `TestCoverage.xml` and `TestCoverageReport`.

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