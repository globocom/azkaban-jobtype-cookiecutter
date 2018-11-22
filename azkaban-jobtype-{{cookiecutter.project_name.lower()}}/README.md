# Azkaban jobtype {{cookiecutter.project_name}}
{{cookiecutter.project_name}} Plugin for [Azkaban](https://github.com/azkaban/azkaban)

## Build

Execute the command:

```sh
./gradlew installDist
```

## Installing

After completion, plugins will be available in `build/install/azkaban-jobtype-{{cookiecutter.project_name.lower()}}`. Move `plugins` directory to `$AZKABAN_HOME` dir (Executor Server). Configure `.properties` files as necessary.
If you already have `$AZKABAN_HOME/plugins` dir on Azkaban Executor Server, just add the necessary files (jars on `plugins/extlib` and configuration files on `plugins/jobtypes/{{cookiecutter.project_name.lower()}}`)

## Usage

#### Admin:

Configurations:

In `private.properties`
```
jobtype.class=azkaban.jobtype.{{cookiecutter.project_name}}Job

```

#### User:

```
type={{cookiecutter.project_name.lower()}}

```