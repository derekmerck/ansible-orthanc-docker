Orthanc-Docker
==============

[![Build Status](https://travis-ci.org/derekmerck/ansible-orthanc-docker.svg?branch=master)](https://travis-ci.org/derekmerck/ansible-orthanc-docker)

Configure and run an [Orthanc](https://www.orthanc-server.com) DICOM node in a Docker container.

Requirements
--------------

Requires Docker, Docker-py and the `docker_image` and `docker_container` modules.

Role Variables
--------------

### Docker Image and Tag

Select an Orthanc image and tag.

- `jodogne/orthanc` is the official vanilla [Orthanc for Docker][] build maintained by Sébastien Jodogne
- `jodogne/orthanc-plugins` is the official build supporting the Postgresql backend
- `osimis/orthanc` is a spin with Osimis's excellent third party web viewer for review and annotation
- `derekmerck/orthanc` is a multi-architecture bleeding edge release spin

[Orthanc For Docker]: http://book.orthanc-server.com/users/docker.html

```yaml
orthanc_docker_image:       "jodogne/orthanc"
orthanc_docker_image_tag:   "latest"
```

### Docker Container Configuration

```yaml
orthanc_container_name:     "orthanc"
orthanc_use_data_container: True
orthanc_data_dir:           "/opt/orthanc/db"
orthanc_config_dir:         "/opt/orthanc"
orthanc_api_port:           8042
orthanc_dicom_port:         4242
orthanc_container_timezone: "America/New_York"
```

### Service Configuration

Configure the service.  These variables are used in the template config file.

```yaml
orthanc_title:              "Orthanc"
orthanc_aet:                "ORTHANC"
orthanc_user:               "orthanc"
orthanc_password:           "passw0rd!"
```

### PostgreSQL Configuration

```yaml
orthanc_pg_backend:         False
orthanc_pg_user:            "orthanc"
orthanc_pg_password:        "passw0rd!"
orthanc_pg_host:            "localhost"
orthanc_pg_port:            5432
```

Dependencies
------------

- `geerlingguy.docker` to setup the docker environment
- `matic-insurance.docker-postgres` to setup the postgres backend, if needed

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - derekmerck.orthanc-docker
```

License
-------

MIT

Author Information
------------------

Derek Merck  
<derek_merck@brown.edu>  
Rhode Island Hospital and Brown University  
Providence, RI  

