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

When you look into a project's source-code the first time you do not want to search for everything.
It is much better when you look into the project and think:
"When I want to compile the project, I know how I can do this.
And when I want to run the unit-tests, I also know how I can do this."
The _non-functional_ things of a project can/should be consistent which helps when new developer familiarize themselves with the project.

Example:

It is like start to work for a new company and you go to the office-building the first time and you know:
Here is the reception, there are the office-rooms and over there is the canteen, because that is how it is in nearly every building.
If you can orientate yourself on one building, you can also do so on all the others that are constructed in exactly the same way.
It does not mean that the people do all the same work in all these buildings, but it is much easier to find your way around.

In reality, there are rarely 2 exactly the same office buildings.
But applying this principle in source-code-repositories is absolutely possible and useful!

IT-related example:

When managing applications for example there is something like a de-facto-standard today:
Docker/Kubernetes.
You do not really care about the internal structure of the application-container.
This internals do not matter (at least for everyday-usage/-issues) because you can manage the containers using the same program with the same interface.
When you want to run an application on your server there is a _requirement_ that the application is runnable in a container to be able to use this interface.
This seems like this is not the best idea for an individual "freedom" of developer or administrators concerning the deployment of their application but this is a good restriction nevertheless because it makes many things much easier.
And this is very useful.

So let us use this principles also for source-code repositories!
It is reasonable to add a few requirements also for structuring git-repositories to implement the next step to make software-development better and easier:

A unique standardized file-structure inside a repository.

This helps everyone to use nearly unique build-pipelines and -scripts, differing only in a few arguments for the build-pipeline-arguments for example.
Management of a repository will be easier because there is less proliferation and more well-known structure.

For this proposals are templates and specifications defined in this repository.
To use it, there is no need to restructure existing projects.
Existing projects can simply be adapted to the standardized repository-structures defined in this repository.
The purpose of this templates-repository is to add additional standards which make standard-tasks (merging, building, etc.) available in a unique standardized-way, applicable for nearly all projects.

## Repository-Conventions

### Structure

This repository implements the structure-requirements defined by [MinimalRequirements](./Templates/Conventions/RepositoryStructure/MinimalRequirements/MinimalRequirements.md).

### Development

#### Branching-system

This repository applies the [MainLine](./Templates/Conventions/BranchingSystem/MainLine.md)-branching-system.
