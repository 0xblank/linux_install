docker rm --force debian_install_test
docker build -t debian_install ./install
docker run --name debian_install_test debian_install