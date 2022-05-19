# ProjectTemplates

This repository contains proposals for structuring sourcecode-repositories managed using [git](https://git-scm.com/).

## Background

Software-development is a big subject with many aspects and many things to consider.
There are also many things grown historically in a very unstructured way.
In the technical implementation of projects we software-developer do many things because of at least one of the following reasons:

- Coding-style- and project-guidelines defined by the company
- Things are grown historically
- One does not know a good project-structure for the specific project
- One does generally not care about a good project-structure
- Competing approaches for that issues will be used parallelly

So nearly every project has a different structure.
So every build-pipeline looks very different and has its own properties.
And this is probably not a good situation.

When managing applications for example there is something like a de-facto-standard today:
Docker/Kubernetes.
You do not really care about the internal structure of the application-container.
It does not matter (for everyday-usage/-issues) because you can manage the containers using the same program with the same interface.
When you want to run an application on your server there is a _requirement_ that the application is runnable in a container.
This seems like this is not the best idea for an individual "freedom" of developer for the deployment of their application but this is a good restriction because it makes many things easier.
And this is very useful.
So let us use this principles also for source-code repositories!
It is reasonable to add a few requirements also for structuring git-repositories to implement the next step to make software-development easier:
A unique standardized file-structure inside a repository.
This helps everyone to use unique build-pipelines and -scripts with only a few parameters.
Management of a repository will be easier because there is less proliferation and more well-known structure.
For this proposals are templates and specifictions defined in this repository.
To use it, there is not need to restructure existing projects.
Existing projects can simply be adapted to standardized repository-structures defined in this repository.
The purpose of this templates-repository to add additional standards which make standard-tasks available in a unique standardized-way, applicable for nearly all projects.

## Repository-Conventions

### Structure

This repository applies requirements defined by [MinimalRequirements](./Templates/Conventions/RepositoryStructure/MinimalRequirements.md).

### Development

#### Branching-system

This repository applies the [MainLine](./Templates/Conventions/BranchingSystem/MainLine.md)-branching-system.
