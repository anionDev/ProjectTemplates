# Common Project Structure

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

- `<codeunit>/Other/InternalScripts/QualityCheck/RunTestcases.py`
- `<codeunit>/Other/TestCoverage/TestCoverage.xml`
- `<codeunit>/Other/TestCoverage/Report`
- `<codeunit>/Other/InternalScripts/QualityCheck/Linting.py`
- `<codeunit>/Other/InternalScripts/Build/Build.py`
- `<codeunit>/Other/InternalScripts/Build/Result`
- `<codeunit>/<codeunit>`
- `<codeunit>/<codeunit>.codeunit`
- `<codeunit>/<codeunit>Tests`

A merge on the main-branch is only allowed if the scripts `RunTestcases.py`, `Linting.py` and `Build.py` exits with 0 for each code-unit.
At the latest when the merge-commit will be done then the following things must be done for each code-unit which has been changed in the merge:

- The `TestCoverage.xml`-file must be updated by running `RunTestcases.py`.
- The version in the `<codeunit>.codeunit`-file must be changed to a higher version.

## Further explanations

### `RunTestcases.py`

It is expected that the file `<codeunit>/Other/InternalScripts/QualityCheck/RunTestcases.py` is a python3-script which exits with a non-zero-exitcode if at least one testcase fails.

If something like compiling is required to run the testcases then this script must do that. These compiled files may be placed neither in the folder `<codeunit>/Other/InternalScripts/Build/Result` nor in any not git-ignored-folder.

This script should generate or update `<codeunit>/Other/TestCoverage/TestCoverage.xml` and `<codeunit>/Other/TestCoverage/Report`.

### `<codeunit>/Other/TestCoverage/TestCoverage.xml`

It is expected that `<codeunit>/Other/TestCoverage/TestCoverage.xml` contains a test-coverage-report of the code-unit in the cobertura-format.

### `<codeunit>/Other/TestCoverage/Report`

It is expected that the folder `<codeunit>/Other/TestCoverage/Report` contains a `index.html` containing a html-report about the unittest-coverage based on `<codeunit>/Other/TestCoverage/TestCoverage.xml`.
The `Report`-folder does not have to be committed.

### `<codeunit>/Other/InternalScripts/QualityCheck/Linting.py`

It is expected that the file `<codeunit>/Other/InternalScripts/QualityCheck/Linting.py` is a python3-script which exits with a non-zero-exitcode if there is at least one linting-issue.

### `<codeunit>/Other/InternalScripts/Build.py`

It is expected that the file `<codeunit>/Other/InternalScripts/Build.py` is a python3-script which creates the build-artefact of the code-unit for productive usage and exits with a non-zero-exitcode if the build fails for any reason.
The build-artefact should be placed in `<codeunit>/Other/InternalScripts/Build/Result`.

### `<codeunit>/Other/InternalScripts/Build/Result`

It is expected that the folder `<codeunit>/Other/InternalScripts/Build/Result` is git-ignored.

### `<codeunit>/<codeunit>`

It is expected that the folder `<codeunit>/<codeunit>` contains the source-code of the code-unit.

### `<codeunit>/<codeunit>.codeunit`

It is expected that the folder `<codeunit>` contains the file `<codeunit>.codeunit` with the following xml-content.

```xml
<codeunit codeunitspecificationversion="1.0.0">
    <name>[codeunit-name]</name>
    <version>[codeunit-version]</version>
</codeunit>
```

While the project-version-specification is defined by [MinimalRequirements](./MinimalRequirements.md) a code-unit-version is independent of the project version but the rules to change code-unit-versions are the same as the rules for changing the project-version. So a code-unit-version can always be the same as the project-version but it does not have to.

### `<codeunit>/<codeunit>Tests`

It is expected that the folder `<codeunit>/<codeunit>Tests` contains the unit-tests of the code-unit.
