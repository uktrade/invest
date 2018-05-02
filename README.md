# Invest
[Invest](https://invest.great.gov.uk/)

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

## Requirements

[Python >= 3.6](https://www.python.org/downloads/release/python-360/)

[Docker >= 1.10](https://docs.docker.com/engine/installation/)

[Docker Compose >= 1.8](https://docs.docker.com/compose/install/)


## Local installation

    $ git clone https://github.com/uktrade/invest
    $ cd invest
    $ make

## Running with Docker
Requires all host environment variables to be set.

    $ make docker_run

### Run debug webserver in Docker

    $ make docker_debug

### Run tests in Docker

    $ make docker_test

### Host environment variables for docker-compose
``.env`` files will be automatically created (with ``env_writer.py`` based on ``env.json``) by ``make docker_test``, based on host environment variables with ``INVEST`` prefix.

## Debugging

### Setup debug environment

    $ make debug

### Run debug webserver

    $ make debug_webserver

### Run debug tests

    $ make debug_test

## CSS development

Currently the site just uses flat css, this was to enable fast development of the website.

Bootstrap4 is used, for the same reason, instead of export-elements.


### Requirements
[node](https://nodejs.org/en/download/)
[gulp](https://gulpjs.com/)
[SASS](http://sass-lang.com/)

	$ npm install
	$ gulp sass

### Update CSS under version control

	$ gulp sass

### Rebuild the CSS files when the scss file changes

	$ gulp sass:watch

### S3 Bucket Permissions

Wagtail stores images on the S3 Bucket, it needs the following permissions to be enabled

	arn:aws:s3:::bucket-name-here
	s3:ListBucket

	arn:aws:s3:::bucket-name-here/*
	s3:PutObject, s3:PutObjectAcl, s3:GetObject, s3:GetObjectAcl, s3:DeleteObject"


## Seeding development content from prod

The site is dependent on the textual content and images, so having a copy
of the live content is helpful.

### Preparation

 Run everything in a fresh terminal session so that settings are not persisted

 - Setup postgres on your local machine.
 - Create an empty database invest

### Copy the database and content

This example clones invest-staging to the database invest

$ ./scripts/clone-site.sh invest-staging postgres://username:password@localhost:invest


[code-climate-image]: https://codeclimate.com/github/uktrade/invest/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/invest

[circle-ci-image]: https://circleci.com/gh/uktrade/invest/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/invest/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/invest/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/invest

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/invest.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/invest
