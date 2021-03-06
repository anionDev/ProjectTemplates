# CommonProjectStructure

## Purpose

`CommonProjectStructure` is an attempt for a standardized repository structure for real-world-usecases and -repositories for source-code. It is designed to contain one or more independent (sub)projects which will be called `codeunit`s. So the repository-structure defined by `CommonProjectStructure` is applicable for small projects but also for large [Monorepo](https://en.wikipedia.org/wiki/Monorepo)s.

## Requirements

The repository must implement the requirements defined by [MinimalRequirements](../MinimalRequirements/MinimalRequirements.md) with the following updates/changes:

The `ReadMe.md`-file must also contain:

- A runtime- and development-dependency-list for all codeunits
- Applied repository-structure
- Applied branching-system
- Information if contribution is allowed/desired and, if yes, which constraints/conventions/conditions are associated with it
- Information about which version of `CommonProjectStructure` will be applied (define to support the "latest" version with the condition to update the repository if the requirements changes is also fine)

Furthermore the repository must contain the following file with appropriate content:

- [`GitVersion.yml`](https://github.com/GitTools/GitVersion)
- [`<projectname>.code-workspace`](https://code.visualstudio.com/docs/editor/workspaces)

If the source-code of the project is publicly available then also the following file must be contained:

- [`.well-known/security.txt`](https://securitytxt.org/)

A codeunit is a compilable part of the project.
Small projects may often have only one codeunit, that is no problem.
A typical modern web-application for example will probably have at least 2 codeunits (e. g. for web-part and backend-part).
Testcases for a codeunit are a mandatory part of the codeunit.

For each codeunit the repository must contain the following files and folder with appropriate content:

- `<codeunit>/<codeunit>.codeunit`
- `<codeunit>/Other/QualityCheck/RunTestcases.py`
- `<codeunit>/Other/QualityCheck/Linting.py`
- `<codeunit>/Other/QualityCheck/TestCoverage/TestCoverage.xml`
- `<codeunit>/Other/Reference/GenerateReference.py`
- `<codeunit>/Other/Reference/ReferenceContent`
- `<codeunit>/Other/CommonTasks.py`
- `<codeunit>/Other/Build/Build.py`

All of these python-scripts are supposed to be executable on every developer-machine without any special software or sensitive data like keys which are typically not available on a development-machine.

Additional to that there are the following folder which must be git-ignored but must be generated by the appropriate scripts listed above:

- `<codeunit>/Other/Build/BuildArtifact`
- `<codeunit>/Other/QualityCheck/TestCoverage/TestCoverageReport`
- `<codeunit>/Other/Reference/GeneratedReference`

`<codeunit>` must be replaced by the name of the codeunit.
There are the following rules for the name of a codeunit:

- It is supposed to be a meaningful English name or abbreviation.
- It must be in [Pascal-case](https://www.theserverside.com/definition/Pascal-case).
- It is primary intended to be a project-internal label

A merge on the main-branch is only allowed if the scripts `CommonTasks.py`, `RunTestcases.py`, `Linting.py`, `GenerateReference.py` exits with 0 for each codeunit.
It is also recommended to run `Build.py` for each codeunit to ensure that the build-script also runs without any errors.

## Further explanations

### Version

The project's version is defined by the output of `gitversion /showVariable MajorMinorPatch`.
The version must be incremented due to the conditions described by [SemVer](https://semver.org/).
Additional to that, the major-version is also be allowed to be increased when large or important features will be added or if it is appropriate for business-reasons.

### Specific files and folders

#### `<codeunit>`

It is expected that the folder `<codeunit>` contains the source-code of the codeunit including its testcases and (if available) the ui-translations of the codeunit (e. g. `.arb`-files or `.xlf`-files).

##### Dependencies

In the source-code of a codeunit it is allowed to directly include (means: referencing and using) the source-code of another codeunit if and only if both codeunits belong to the same project and are stored in the same repository.
A codeunit is not allowed to have uncommon external dependencies which are not available in the dependency-manager of the used programming-language and which are usually not available on a development-machine or a machine where the codeunit is expected to be executed on in a productive environment.

##### Codeunit-internal Conventions

If there is no hard defined project-structure defined by the programming-language or other "external circumstances" then the following sub-file-structure is recommended:

- `<codeunit>/<codeunit>`: Folder for the source-code
- `<codeunit>/<codeunit>Tests`: Folder for the testcases
- `<codeunit>/Other/Translations`: Folder for ui-translations of the codeunit.
- `<codeunit>/Other`: Folder for all other things including scripts and resources.

If the used programming language provides a specific sourcecode-structure recommended by the maintainer of the used programming-language/framework then it is recommended to follow these conventions.
This recommendation still applies if even the recommendations are contrary to the other regulations described here.
The purpose of this is that some programming languages enforce a more or less strictly defined structure.
It is often advisable to follow them and sometimes nearly impossible to not follow them.
But it is definitely impossible in practice to find two programming languages or frameworks which have exactly the same project-structure, style-guide, etcetera which makes it simply impossible to have a unique file-structure over the entire project/repository if you have at least 2 codeunits which require another programming-language (e.g. for frontend and backend).

The aim of the `CommonProjectStructure` is to be flexible and usable for many programming languages and frameworks, no matter what their requirements and recommendations say.
Style-mixtures are inevitable when you use different programming languages and this is absolutely fine because on the one hand this is normal and no real problem in practice.
And on the other hand codeunits should be independent and there is no requirement to adjust the structure and style of a codeunit to another not recommended structure and style.
But the style of codeunits can (and is supposed to) be consistent inside itself over the entire codeunit.

#### `CommonTasks.py`

It is expected that the file `CommonTasks.py` is a python3-script which exits with a non-zero-exitcode if it fails.
This script is supposed to do things like update the version in `<codeunit>.codeunit` or other files of the codeunit.

#### `RunTestcases.py`

It is expected that the file `RunTestcases.py` is a python3-script which exits with a non-zero-exitcode if at least one testcase fails. This script does not have to check the minimum test-coverage defined by `<codeunit>.codeunit` (because this is a task of a merge-script).

If something like compiling is required to run the testcases then this script must also do that. These compiled files may not be placed in git-ignored-folder.

This script must generate or update `TestCoverage.xml` and `TestCoverageReport`.

#### `TestCoverage.xml`

It is expected that `TestCoverage.xml` contains a test-coverage-report of the codeunit in the cobertura-format.

#### `TestCoverageReport`

It is expected that after running `RunTestcases.py` the folder `TestCoverageReport` contains a `index.html` containing a html-report about the unittest-coverage based on `TestCoverage.xml`.
The `TestCoverageReport`-folder must be git-ignored.

#### `Linting.py`

It is expected that the file `Linting.py` is a python3-script which exits with a non-zero-exitcode if there is at least one linting-issue.

#### `GenerateReference.py`

It is expected that the file `GenerateReference.py` is a python3-script which generates or updates the reference based on `ReferenceContent` in `GeneratedReference` and exits with a non-zero-exitcode if at least one error occurs.

#### `ReferenceContent`

The folder `ReferenceContent` must contain a reference for the codeunit. The content of this folder is the source of the `GeneratedReference`-folder.
The `ReferenceContent`-folder must be committed.

#### `GeneratedReference`

It is expected that after running `GenerateReference.py` the folder `GeneratedReference` contains an `index.html`-file (and possibly other files) containing a html-reference of the codeunit based on `ReferenceContent`.
The `GeneratedReference`-folder must be git-ignored.

#### `Build.py`

It is expected that the file `Build.py` is a python3-script which creates the build-artefact of the codeunit for productive usage and exits with a non-zero-exitcode if the build fails for any reason.
The build-artefact must be placed in `BuildArtifact`.
Pushing the build-artifact to a package-registry/build-artifact-feed or something like this is not a task for this script.

#### `BuildArtifact`

The folder `BuildArtifact` must be git-ignored.

#### `<codeunit>.codeunit`

It is expected that the folder `<codeunit>` contains the file `<codeunit>.codeunit` with the following xml-content:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<codeunit:codeunit codeunitspecificationversion="1.0.0" xmlns:codeunit="https://github.com/anionDev/ProjectTemplates" xmlns:schemaLocation="https://raw.githubusercontent.com/anionDev/ProjectTemplates/main/Templates/Conventions/RepositoryStructure/CommonProjectStructure/codeunit.xsd">
    <codeunit:name>codeunit</codeunit:name>
    <codeunit:version>1.0.0</codeunit:version>
    <codeunit:minimalcodecoverageinpercent>90</codeunit:minimalcodecoverageinpercent>
</codeunit:codeunit>
```

The values inside the xml-document must obviously be adapted.

While the project-version-specification is defined by [MinimalRequirements](./MinimalRequirements.md) a codeunit-version is independent of the project version but the rules to change codeunit-versions are the same as the rules for changing the project-version. So a codeunit-version can always be the same as the project-version but it does not have to.

### Language

The only language which is allowed to be used in the repository is English.
This comprises the entire committed content including source-code, markdown-files, license-files, folder-names, etcetera.
The only exceptions of this rule are certain labels (such as the project name for example) and the content of ui-translations for obvious reasons.
