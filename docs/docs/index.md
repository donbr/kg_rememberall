# kg_rememberall documentation!

## Description

A structured repository for exploring and capturing insights across knowledge graphs, machine learning, data engineering, and generative AI

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://s3://kg-rememberall/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://s3://kg-rememberall/data/` to `data/`.


