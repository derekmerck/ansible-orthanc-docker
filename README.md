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
- `jodogne/orthanc-plugins` is the official build supporting the Postgresql backend
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

