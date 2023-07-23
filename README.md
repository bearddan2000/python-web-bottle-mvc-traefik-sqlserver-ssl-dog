# python-web-bottle-mvc-traefik-sqlserver-ssl-dog

## Description
Simple web app that serves static pages
for a bottle project.

Uses sqlalchemy query a table `dog`.

Sql server uses self-signed ssl.

## Tech stack
- python
  - bottle
  - sqlalchemy
- bootstrap
- jquery
- dataTable
- mssql
- ssl

## Docker stack
- alpine:edge
- alpine:edge
- python:latest
- traefik:v2.4
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- [Availble at](https://myapi.docker.localhost)

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
[Bottle sqlalchemy setup](https://github.com/iurisilvio/bottle-sqlalchemy/blob/master/examples/basic.py)
