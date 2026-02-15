# NXLog Logging POC

## Overview

This POC demonstrates how **NXLog handles log forwarding during network interruptions / log censoring**.

The environment is fully simulated using Docker and consists of:

- **Fake Log Producer (logger)** – generates (simulated)log file entries to /logs/app.log, shared as volumes
- **Logger (nxlog)** – reads and forwards logs (by log producer), does needed (configured) log censoring
- **Store Log Target System (log-target)** – receives network forwarded (and censored) logs for observing 

The goal is to test reliability and behavior when the network connection between components is disrupted. And if log files can be censored before sending to observer/control center


Log producer (fake application) ---via file---> NXLog ---via network--> Logs observing system

---

## System commands

**Build:** `docker-compose build`

**Run:** `docker-compose up `   

**Stop:** `docker-compose down -v`

---

### **Log files , usage commands**

**NXLog collected log files:** 
`tail -f /var/lib/docker/volumes/loggersystem_nxlog_out/_data/collected.log` 

or

`docker-compose exec nxlog tail -f /nxlog/out/collected.log`

**Docker Network info:**

`docker network ls`

`docker network inspect loggersystem_default`


**Disconnect network from NXLog to logger system:**

`docker network disconnect loggersystem_default log-target`

**Reactivate network**

`docker network connect loggersystem_default log-target`


**Observe missing logs (due breakage time) to appear into received log:**

`docker exec -it log-target tail -f /logs/received.log`

Observe also ERROR log type has been censored properly!


## Example logs

**Generated log example:**

```
nxlog        | 2026-02-15 09:48:39 WARNING om_tcp received data from remote end (got 53 bytes)
nxlog        | 2026-02-15 09:48:39 WARNING om_tcp received data from remote end (got 53 bytes)
fake-logger  | 2026-02-15 09:48:49 [DEBUG] Test message number 23347
nxlog        | 2026-02-15 09:48:49 WARNING om_tcp received data from remote end (got 54 bytes)
nxlog        | 2026-02-15 09:48:49 WARNING om_tcp received data from remote end (got 54 bytes)
fake-logger  | 2026-02-15 09:48:59 [ERROR] Test message number 17173
```


**Received censored log example:**

```
2026-02-15 09:48:39 [WARN] Test message number 28657
2026-02-15 09:48:49 [DEBUG] Test message number 23347
[SENSUROITU] Number:17173
2026-02-15 09:49:09 [INFO] Test message number 31698
2026-02-15 09:49:19 [INFO] Test message number 31392
2026-02-15 09:49:29 [DEBUG] Test message number 5527
```