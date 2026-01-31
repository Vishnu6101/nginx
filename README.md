# NGINX + FastAPI (Docker) — Production-Style Setup

This README walks through a **clean, production-grade setup** using **NGINX (Docker)** in front of **FastAPI**, implementing:

* ✅ Static file serving (handled by NGINX)
* ✅ Reverse proxy (NGINX → FastAPI)
* ✅ Load balancing across multiple FastAPI instances

This architecture mirrors how real systems are deployed in **cloud platforms, Kubernetes, and large-scale backend services**.

---

## High-Level Architecture

```
Client / Browser
      |
      v
NGINX (Docker)
  ├── /static  → Static files
  └── /api     → Reverse proxy
                     |
                     v
            Load balancer (NGINX)
            ├── FastAPI instance 1
            └── FastAPI instance 2
```

NGINX is the **single entry point** exposed to the internet.
FastAPI instances remain **private and isolated**.

---

## Why This Architecture?

* NGINX excels at handling **connections, TLS, static assets, and routing**
* FastAPI focuses purely on **application logic**
* Horizontal scaling is easy (add more FastAPI instances)
* Matches real production patterns (Ingress / API Gateway model)

---

## Project Structure

```
nginx-fastapi/
├── docker-compose.yml
├── nginx/
│   └── nginx.conf
├── app/
│   ├── Dockerfile
│   └── main.py
└── static/
    └── hello.txt
```

---

### Key Responsibilities of NGINX

* Accepts all incoming traffic
* Serves static files efficiently
* Acts as a reverse proxy
* Load balances requests using `least_conn`
* Preserves client request metadata via headers

---

### Notes

* `ro` mounts ensure configs and static files are **read-only**
* Docker DNS resolves `app1` and `app2` automatically
* NGINX load balances traffic across both services
* Static assets are served **directly by NGINX**, bypassing FastAPI entirely.

---

## Running the System

```bash
docker compose up --build
```

NGINX will be available at:

```
http://localhost:8080
```

---

## Testing the Setup

### Static File Serving

```
http://localhost:8080/static/hello.txt
```

Served directly by NGINX.

---

### Reverse Proxy + Load Balancing

```
http://localhost:8080/api/health
```

Refresh multiple times — you should see different `served_by` values.

This confirms load balancing is working.

---

## What I’ve Built

* ✔ Event-driven NGINX frontend
* ✔ FastAPI backends isolated from the internet
* ✔ Load-balanced architecture
* ✔ Static assets served efficiently
* ✔ Production-style traffic flow

This is the **same foundational pattern** used by:

* Cloud load balancers
* Kubernetes ingress controllers
* API gateways

---

## Key Takeaway

> NGINX is not just a web server.
> It is a **high-performance traffic router** that sits in front of your applications and lets them scale safely.

---

## References
[NGINX - Zero To Hero: Your Ultimate Guide from Beginner to Advanced Mastery](https://medium.com/@ksaquib/nginx-zero-to-hero-your-ultimate-guide-from-beginner-to-advanced-mastery-57e2dad6a77a)