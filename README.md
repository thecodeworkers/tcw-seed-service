
Add in docker compose following lines

```
seed_services:
    container_name: tcw_seed_services
    build: ./tcw-seed-services
    command: python -u run.py
    environment: 
    - DATABASE_HOST=mongodb
    - DATABASE_PORT=27017
    volumes:
    - ./tcw-seed-services:/usr/app
    depends_on:
    - mongodb
```
