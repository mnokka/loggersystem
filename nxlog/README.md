# NXLog-CE docker version

## NOTE

* NXLog-CE docker version is based on the latest CentOS 7 base image.
* The build process uses the NXLog-CE RHEL 7 version.

## Build a standalone version

* Build command: `docker build -t nxlog-ce .`

## Run the NXLog-CE Agent

* Start the container: `docker run -p <HostPort>:<ContainerPort> -d nxlog-ce`

## Customization

* Custom configuration file can be attached as a volume when running the container: `docker run -p <HostPort>:<ContainerPort> -v $(pwd)/nxlog.conf:/etc/nxlog/nxlog.conf -d nxlog-ce`
* The default configuration file can be overriden with `-c <PATH-TO-CONFIG>` when starting the container.
* Ports can be opened with `-p <HostPort>:<ContainerPort>` when starting the container. NOTE: The default user for running NXLog-CE is `nxlog` and that user does not have administrative rights to access ports under *1024*. To use ports under *1024* the `USER nxlog` line must be removed from the `Dockerfile`
* For more information refer to the [docker run](https://docs.docker.com/engine/reference/commandline/run/) documentation.
