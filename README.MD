# NXLog Logging POC

## Overview

This POC demonstrates how **NXLog handles log forwarding during network interruptions**.

The environment is fully simulated using Docker and consists of:

- **Log Producer** – generates log file entries (Fake Logger)
- **Logger (NXLog)** – reads and forwards logs
- **Log Target System** – receives forwarded logs

The goal is to test reliability and behavior when the network connection between components is disrupted.

---

## Fake Logger

The **fake logger** simulates an application that continuously writes log entries to a file.

It produces a stream of generated log data into: /logs/app.log (volumes fake_logs )


**Build:** `docker-compose build`

**Run:** `docker-compose up `     -d to detach

**Stop:** `docker-compose down`

**Logs:**  `docker-compose logs -f`

**NXLog Collected logs files:** 

`tail -f /var/lib/docker/volumes/loggersystem_nxlog_out/_data/collected.log` 
`docker-compose exec nxlog tail -f /nxlog/out/collected.log`





