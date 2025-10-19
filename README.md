# TP-cloud-native-fastapi-duo

# Salida Tests 
#   Users API
```bash
docker exec -it users-api pytest -q
.                                                            [100%]
1 passed, 3 warnings in 0.75s

# Salida curls
dani15@Dani-PC:/mnt/c/Users/danie/Desktop/cloud-native-fastapi-duo$ curl -X POST http://localhost:8001/users -H "Content-Type: application/json" -d '{"name":"Ada","email":"ada@example.com"}'

dani15@Dani-PC:/mnt/c/Users/danie/Desktop/cloud-native-fastapi-duo$ curl -X POST http://localhost:8002/orders -H "Content-Type: application/json" -d '{"user_id":1,"item":"Book","qty":2}'ser_id":1,"item":"Book","qty":2}'
{"id":2,"user_id":1,"item":"Book","qty":2}

dani15@Dani-PC:/mnt/c/Users/danie/Desktop/cloud-native-fastapi-duo$ curl http:curl http://localhost:8001/users
[{"id":1,"name":"Ada","email":"ada@example.com"}]

dani15@Dani-PC:/mnt/c/Users/danie/Desktop/cloud-native-fastapi-duo$ curcurl http://localhost:8002/orders
[{"id":1,"user_id":1,"item":"Book","qty":2},{"id":2,"user_id":1,"item":"Book","qty":2}]