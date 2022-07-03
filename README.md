# Deploy odoo 13 in production using Docker Compose


## How to use it 

### Without the db container (recommended)

 
- Clone this repository:

```bash
git clone --branch odoo https://github.com/yassine125/DevopsTools.git
```

- Update the `config/odoo.conf` with your custom params like `admin_passwd`, `dbfilter` ..

- clone your custom addons  to `extra-addons` folder.

- Create the odoo Network if does not exist

```bash
docker network create odoo 
```

- Start container on production env

```bash
$ docker-compose  up -d
```

- Start container on dev env

```bash
$ docker-compose up -d --build
```
