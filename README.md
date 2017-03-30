# Sublime Text Package for Cucumber

## How to Install

Clone/Extract this repository to your Sublime Text 3 Packages folder

> Preferences -> Browse Packages to open folder

## Features

### Run Cucumber

This command is the same as running `cucumber` and run all cucumber testing scenarios at recently opened file project root (where `features` folder exist). Run it via:

`Tools > CucumberTestingBundle > Run Cucumber`

### Run Current File

Run `cucumber` targeting the active view, same as `cucumber <file_name>`. Run it via:

`Tools > CucumberTestingBundle > Run Current File` or `Alt + Shift + C` (by default)

### Run Current Line

Run `cucumber` targeting the active view and active line, same as `cucumber <file_name>:<line_number>`. Run it via:

`Tools > CucumberTestingBundle > Run Current Line` or `Alt + Shift + L` (by default)

### Run Last Test

Running previous command run by `CucumberTestingBundle`. Run it via:

`Tools > CucumberTestingBundle > Run Last Test` or `Alt + Shift + Z` (by default)
