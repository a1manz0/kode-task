### Getting Started 
#### First you need to clone this repository
```
git clone https://github.com/a1manz0/kode-task.git
```
#### Then run
```
docker compose up --build
```

### To register you can use:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/auth/register' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "email": "email",
  "password": "string",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false
}'
```

### To get access token you can use:
```
curl -X 'POST'   'http://127.0.0.1:8000/auth/jwt/login'   -H 'accept: application/json'   -H 'Content-Type: application/x-www-form-urlencoded'   -d 'username=email&password=string'
```

### To create note you can use:
```
curl -X 'POST' 'http://127.0.0.1:8000/notes/add' -H 'accept: application/json' -H 'Content-Type: application/json' -H'Authorization: Bearer YOUR_TOKEN'  -d '{"content": "some content with errars" }'
```

### To get all notes you can use:
```
curl -X 'GET' 'http://127.0.0.1:8000/notes/get_all' -H 'accept: application/json' -H'Authorization: Bearer YOUR_TOKEN'
```
