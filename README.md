# Data Models Workshop

## Table of Contents
1. [Setup](#setup)
2. [Testing](#testing)
    1. [Unit Testing](#unit-testing)
    2. [Integration Testing](#integration-testing)
    3. [Manual Testing](#manual-testing)
3. [CI/CD](#cicd)
    1. [CI](#ci)
4. [Code Structure](#code-structure)
5. [Git Development](#git-development)

## Context
_This workshop took place as part of the [TechBiz](https://thinkbiz.gr/projects/techbiz/) event for [ThinkBiz](https://thinkbiz.gr/). The presentation, titled: `Bridging the Gap: Translating Business Needs into Data Models with Python & PostgreSQL`, explored the concepts of Domain Modeling and Database Architecture using industry-standard tools, including Python, PostgreSQL, ORM, and GitHub.  As we embarked on hands-on exercises that simulated real-world engineering challenges, much of the work in this repository has been co-authored and contributed by my colleague, Alexandros Ntelifilippidis ([github](https://github.com/alexntelifilippidis), [linkedin](https://www.linkedin.com/in/alexandros-ntelifilippidis-98356219a/)). To learn more about 3-tier architecture, check [multi-tier-architecture](https://en.wikipedia.org/wiki/Multitier_architecture)_

## Setup
### Prerequisites

Based on your operating system, please have the following installed on your machine:

#### Editor of your Choice
- Install [VS Code](https://code.visualstudio.com/download) or your preferred editor

#### Git
- Install [Git](https://git-scm.com/downloads)

#### Python
- Install [Python](https://www.python.org/downloads/)

#### Docker Compose
- Install [Docker Compose](https://docs.docker.com/compose/install/)

#### pgAdmin
- Install [pgAdmin](https://www.pgadmin.org/download/). pgAdmin is used to view and manage the PostgreSQL database. In order to set it up correctly you need to add the `.env.variables` values in each option.

### Development Environment
Once you have the prerequisites installed, you can set up your development environment.
Open a terminal and navigate to the project directory

```bash
cd data-models-workshop
```

To get started with the project, you first need to clone it to your local machine. You can do this by running:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

Then you need to create and switch to a new branch. This ensures that the main branch remains clean and deployable at all times:

```bash
git checkout -b <feature-name>   # for features
```

Or by using a GUI tool, e.g. VS Code has a built-in Git GUI.

#### pyenv
- It is recommended to use [pyenv](https://github.com/pyenv/pyenv), a CLI tool that allows multiple versions of Python to be
  installed separately. Follow the [installation instructions](https://github.com/pyenv/pyenv#installation)
  for your platform and run:

  ```
  pyenv install
  ```

- This will download and install Python **3.10.11** which is specified in the `.project-version` file which in turn is created by the command `pyenv local 3.10.11`. This use of pyenv ensures the pinning and usage of the specified Python version.

  > Note: pyenv downloads and compiles the version of Python you install, which means you may need
  > to also install some libraries if not present in your system, please follow the
  > [common build problems wiki](https://github.com/pyenv/pyenv/wiki/Common-build-problems) for
  > your platform.
  > 
  > If you already have Python 3.10.11 installed you do not need to reinstall it and pyenv should automatically use the correct version due to the pinning file `.project-version`

- Create a virtualenv:

  ```bash
    python -m venv .venv
    source .venv/bin/activate
  ```
  > This virtualenv now has the version of Python which was set by pyenv and the .project-version file.
  >
  > Note: the rest of these instructions assume you've activated the virtualenv as does the Makefile. You may want to use a virtualenv tool like
  > [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) or
  > [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv).
  
- Install dependencies via:

```bash
  make install-dev
```

  > Please do not use pip by hand as the makefile contains the explicit activation of pre-commit hooks which will be necessary.

- Run tests to ensure everything is set up correctly:

```bash
  make tests
```

- Create a development version:

``` bash
  make create-dev
```

- Execute a demo service:
  
``` python
  python main.py
```

### Setup operational event database

_The following are advanced instructions for setting up the operational event database. If you are not working on the operational event database, you can skip this section._

Change the environment variable OPERATIONAL_DB_URL to point to the proper PostgreSQL database. By default points to the one
used for integration testing, in [docker-compose-test.yaml](docker-compose-test.yaml) as 

```text
postgresql://postgres:example@localhost:5432/postgres
```

If there are special character in password/username like the ones provided by AWS, you need to url encode them
through some service , e.g. [here](https://www.urlencoder.org/).


## Testing

### Unit Testing

Tested with python 3.10.11.

```bash
  pip install -r requirements.txt
```

- Run all tests with:

```bash
  make unit
 ```

### Integration Testing

Part of the automated tests. If you need to test manually, it is as easy as executing

```bash
  make integration
```

or specifically

```bash
    docker compose -f docker-compose-test.yaml up -d --wait

	echo "Running integration tests"
	pytest -v -s tests/integration --no-header -vv || (make integration-teardown && exit 1)
	echo "Tearing down environment"
	docker-compose -f docker-compose-test.yaml down -v

	echo "Clearing caches"
	make clear
```

The integration tests need a running environment consisting of:

- An operational events postgres database    

The test is trying to add an object in DB and retrieve it. These test roles are already present in [docker-compose-test.yaml](docker-compose-test.yaml)

To run both unit and integration together run:

```bash
  make tests
```

### Manual Testing

Here we run manually the steps leading to the integration tests. This can be useful for debugging purposes and local development.
To create a local environment with prepopulated test data you can run:

```bash
  make create-dev
```

You can find:

- the postgres database on localhost:5432, username is `myuser` and password `mypassword` as per the `.env.variables` file

(if you need things to be stateful, uncomment postgres and mssql volumes on the [docker-compose-test.yaml](docker-compose-test.yaml) file)


## CI/CD

The CI/CD pipeline is configured in the [GitHub actions](.github/workflows) files.

### Continuous integration (CI)
The CI pipeline is configured in the [GitHub actions](.github/workflows/ci.yml) file.:

- It is triggered on every push to the main branch and in every pull request(pr).
- It runs  unit testing and the integration testing.
- It also runs the pre-commit hooks to ensure that the code is formatted correctly and that the tests pass before pushing to the main branch.
- Fails if any of the tests fail.

_No Continuous Deployment (CD) pipeline is configured yet. We lied sorry :)_


## Code Structure

```
.
├── Dockerfile                   # Docker configuration for building a containerized application
├── LICENSE.txt                  # The license under which the software is released
├── Makefile                     # Contains commands to automate common development tasks
├── README.md                    # Repository documentation with introduction, usage, etc.
├── app                          # Main application code
├── artifacts                    # Supplementary files that support the application
├── data                         # Directory for data-related files
├── docker-compose-test.yaml     # Docker Compose configuration specifically for testing environment
├── docker-compose.yaml          # Docker Compose configuration for local development and deployment
├── pyproject.toml               # Configuration and metadata for Python projects, often used with poetry
├── pytest.ini                   # Configuration file for pytest (testing framework)
├── requirements.txt             # List of Python dependencies
├── setup.cfg                    # General configuration file for Python tools and setup
└── tests                        # Test suite for the application     
```

## Git Development

To ensure smooth development and collaboration, it's essential to familiarize yourself with Git operations. Below are some of the most commonly used Git commands in this workflow:

### 1. Clone the Repository

To get started with the project, you first need to clone it to your local machine:

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### 2. Navigate to the Project Directory

Once cloned, navigate to the project directory:

```bash
cd <repository-name>
```

### 3. Create a New Branch

Before starting your work, create a new branch. This ensures that the main branch remains clean and deployable at all times:

```bash
git checkout -b feature/<feature-name>   # for features
git checkout -b bugfix/<bug-name>       # for bug fixes
```

### 4. Check Branch Status

You can always check which branch you're currently on and see if there are changes to commit:

```bash
git status
```

### 5. Add and Commit Changes

After making your changes, stage them for a commit:

```bash
git add .  # stages all changes in the current directory
```

Then, commit your changes with a descriptive message:

```bash
git commit -m "A meaningful description of what was done"
```

### 6. Push Changes to a Remote Repository

Once you've committed your changes, push them to the remote repository:

```bash
git push -u origin <branch-name>
```

### 7. Switching Between Branches

To switch from one branch to another:

```bash
git checkout <branch-name>
```

### 8. Update Your Local Repository

Regularly pull from the main branch to get the latest changes:

```bash
git checkout main
git pull
```

### 9. Merging Changes from Main into Your Branch

If you need to merge changes from the main branch into your current branch:

```bash
git merge main
```

### 10. Deleting a Branch
If you need to delete a branch after merging it into main:

```bash
git branch -d <branch-name>
```

### 11. Viewing Commit History

To see a log of all commits:

```bash
git log
```

For a more concise view with a graphical representation of the commit tree:

```bash
git log --oneline --graph --all
```

### 12. Viewing All Branches

To list all local branches:

```bash
git branch
```

To list all remote branches:

```bash
git branch -r
```

To list both local and remote branches:

```bash
git branch -a
```

### 13. Fetching Changes

Fetch changes from the remote repository without merging them:

```bash
git fetch
```

This is useful to see changes that are on the remote repository but not in your local repository yet.

### 14. Reverting Changes

To undo the changes from the last commit:

```bash
git reset --hard HEAD~1
```

### 15. Stashing Changes

If you're not ready to commit changes but need a clean working directory (e.g., to switch to another branch):

```bash
git stash
```

To apply the stashed changes back into your working directory:

```bash
git stash pop
```

### 16. Set Upstream for Your Branch

If it's your first time pushing a branch to the remote repository, you might need to set the upstream:

```bash
git push --set-upstream origin <branch-name>
```

### 17. Comparing Changes

To see the differences between your working directory and the last commit:

```bash
git diff
```

To see the differences between your staged changes and the last commit:

```bash
git diff --staged
```

---

For more information, check out the [Git documentation](https://git-scm.com/doc).
