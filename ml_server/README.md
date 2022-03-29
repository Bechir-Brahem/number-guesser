you can view the project on: https://number-guesser-ml.herokuapp.com/


this is subdirectory contains the Machine learning server  
the server takes a digit in a format like MNIST and then it performs   
number recoginition using various techniques like CNN,Monte Carlo Dropout, ANNs, random forests...

the ML server is deployed on a VM in azure
to view available models goto:
https://ml-server.westeurope.cloudapp.azure.com/list



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

