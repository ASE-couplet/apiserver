# 测试方法
假设服务器在 `127.0.0.1:8000`。
```
curl http://127.0.0.1:8000/api/upload -F image=@/path/to/your/file
curl http://127.0.0.1:8000/api/result?order=<id>
```
