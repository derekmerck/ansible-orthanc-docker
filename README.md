Ansible Role for Orthanc in Docker
=================================

[![Build Status](https://travis-ci.org/derekmerck/ansible-orthanc-docker.svg?branch=master)](https://travis-ci.org/derekmerck/ansible-orthanc-docker)

Derek Merck  
<derek_merck@brown.edu>  
Rhode Island Hospital and Brown University  
Providence, RI  

Configure and run an [Orthanc](https://www.orthanc-server.com) DICOM node in a Docker container.


Dependencies
--------------

### Galaxy Roles

- [geerlingguy.docker](https://github.com/geerlingguy/ansible-role-docker) to setup the docker environment
- [geerlingguy.pip](https://github.com/geerlingguy/ansible-role-pip) to install Python reqs 
- [matic-insurance.docker-postgres](https://github.com/matic-insurance/ansible-docker-postgres) to setup the postgres backend, if needed


### Remote Node

- [Docker][]
- [docker-py][]

[Docker]: https://www.docker.com
[docker-py]: https://docker-py.readthedocs.io


Role Variables
--------------

### Docker Image and Tag

Select an Orthanc image and tag.

- `jodogne/orthanc` is the official vanilla [Orthanc for Docker][] build maintained by Sébastien Jodogne
- `jodogne/orthanc-plugins` is the official build supporting the Postgresql backend (uses PostgreSQL 10 -- trusty has a problem with installing tools for 9.5)
- `osimis/orthanc` is a third-party [Osimis for Docker][] spin with an excellent web viewer for review and annotation
- `derekmerck/orthanc` is a third-party multi-architecture (amd64, arm32v7) bleeding-edge release spin from [diana-plus][]

[Orthanc For Docker]: http://book.orthanc-server.com/users/docker.html
[Osimis for Docker]: https://osimis.atlassian.net/wiki/spaces/OKB/pages/26738689/How+to+use+osimis+orthanc+Docker+images
[diana-plus]: https://github.com/derekmerck/diana_plus

```yaml
orthanc_docker_image:       "jodogne/orthanc"
orthanc_docker_image_tag:   "latest"
```

### Docker Container Configuration

```yaml
orthanc_container_name:     "orthanc"
orthanc_use_data_container: True
orthanc_data_dir:           "/data/{{ orthanc_container_name }}"
orthanc_config_dir:         "/opt/{{ orthanc_container_name }}"
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
orthanc_pg_user:            "{{ orthanc_user }}"
orthanc_pg_password:        "{{ orthanc_password }}"
orthanc_pg_database:        "{{ orthanc_container_name }}"
orthanc_pg_host:             "postgres"
orthanc_pg_port:             5432
```


Example Playbook
----------------

Run a single orthanc instance.

```yaml
- hosts: dicom_node
  roles:
     - derekmerck.orthanc_docker
```

Run multiple instances against the same backend for load balancing.

```yaml
- hosts: dicom_node
  tasks:
  - include_role:
      name: derekmerck.orthanc_docker
    vars:
      # Independent variables
      orthanc_api_port:        "804{{ item }}"
      orthanc_dicom_port:      "424{{ item }}"
      
      # Shared variables
      orthanc_data_dir:        "/data/orthanc"
      orthanc_docker_image:    "jodogne/orthanc-plugins"
      orthanc_pg_backend:      True
      orthanc_db_name:         "orthanc"
    with_sequence: count=3
```


License
-------

MIT

