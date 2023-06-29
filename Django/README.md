docker build -t django_dev:1.0 ./

docker run -dit -p 8000:8000 --user ta:ta --mount type=bind,source=/Volumes/SourceFiles/devSource/develop/Django/source,target=/home/ta/source --privileged --name django_dev django_dev:1.0
