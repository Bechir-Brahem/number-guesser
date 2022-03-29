generate ssl keys with this command:
```
openssl req -x509 -nodes -days 800 -newkey rsa:2048 -keyout selfsigned.key -out selfsigned.crt
```

run https production server:
 ```
gunicorn --certfile=./selfsigned.crt --keyfile=./selfsigned.key --bind 0.0.0.0:443 number_guesser.wsgi
 ```

the azure vm has 1GB ram very limited
when installing the dependencies the process might be killed automatically.
we can install the tensorflow package with this command
```
pip install tensorflow --no-cache-dir
```

