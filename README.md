# Sublime Text Package for Cucumber

## How to Install

Clone/Extract this repository to your Sublime Text 3 Packages folder

> Preferences -> Browse Packages to open folder

## Features

### How to Run

Features listed below can be triggered and found from these ways:

- Menu: `Tools > CucumberTestingBundle`
- Command Palette: `Ctrl + Shift + P` and enter `CucumberTestingBundle`

---

### Run Test

#### Run Cucumber

This command is the same as running `cucumber` and run all cucumber testing scenarios at recently opened file project root (where `features` folder exist).

#### Run Current File

Run `cucumber` targeting the active view, same as `cucumber <file_name>`.

#### Run Current Line

Run `cucumber` targeting the active view and active line, same as `cucumber <file_name>:<line_number>`.

#### Run Last Test

Running previous command run by `CucumberTestingBundle`.

---

### Tags

#### Run Tags

Run `cucumber` command and append inputted tags after it, same as `cucumber <tags>`

#### Run Current File With Tags

Run `cucumber` targeting the active view, same as `cucumber <file_name> <tags>`

#### Set Default Tags

Set (and overwrite, if existed) default tags that will be displayed when running `Run Tags` and `Run Current File With Tags`
