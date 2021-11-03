# Overview

This repository is intended to supply a baseline Ada coding standard.
It uses the Sphinx/docutils build structure to generate a document in
the user's desired format.

# Content

## Top-level directory

   README.md
      This file

   make.bat
      ``sphinx-build`` build script for Windows

   Makefile
      Makefile to use with ``sphinx-build``

   original.docx
      Original Word document that this repository used as a baseline

## Tools

This folder currently contains a python script that will generate a map file that
parses the source files looking to connect coding standards to ``gnatcheck`` rules.

## Source 

This folder contains the source files necessary to generate the coding standards.

Most of the files should be fairly boilerplate. The directory of most interest is
the ``guidelines`` folder, which contains all of the actual coding standards, grouped
by area of concern.

**Note: If you add a new file into the ``guidelines`` folder, make sure you update the
``guidelines.rst`` file accordingly**

