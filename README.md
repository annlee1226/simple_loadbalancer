# NGINX Load Balancer Demo

Minimal demo of NGINX round-robin load balancing with automatic failover across 3 Flask backends.

## Run

```bash
docker-compose up --build
```

## Test Round-Robin

```bash
# Test load balancer multiple times. Each response shows a different container hostname
curl localhost:8080
curl localhost:8080
curl localhost:8080
```

## Test Failover

```bash
# Stop one backend
docker stop simple_loadbalancer-backend2-1

# Requests still ends up working. NGINX skips the backend that went down.
curl localhost:8080

# Bring back the backend that went down 
docker start simple_loadbalancer-backend2-1
```

## Stop

```bash
docker-compose down
```
