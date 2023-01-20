#   Debian install

Simple scripts I did to ease my debian installations after too much of them done manually. I made these scripts for debian as it's my OS but I guess they should be usable with debian bases distributions. 

> The docker and the build things are just here for testing purposes.

##  How to use

```
# apt install git
$ git clone https://github.com/0xblank/debian_install.git
# ./install/entrypoint.sh
```

> The script must be run as with root privileges so it can install packages and everything

You can edit the packages and git_repositories files to install your own packages and git repositories.

##  How to contribute

Create an issue or a pull request and I will check it out.

##  TO DO list

- [ ] Add git repositories
- [ ] Add debian repositories for
    - [ ] codium
    - [ ] lspci
    - [ ] firmware_iwlwifi
    - [ ] poetry
- [ ] Put config files in the right spots
    - [ ] i3
    - [ ] terminator
- [ ] Make custom installs
    - [ ] Docker
    - [ ] Starship
    - [ ] Vagrant
    - [ ] Exegol
    - [ ] Burp
    - [ ] (maybe) VM ware workstation pro
    - [ ] (maybe) virtualbox
    - [ ] Vagrant
    - [ ] Obsidian
- [ ] Generate rsa keys pairs
    - [ ] github
    - [ ] gitlab
- [ ] Check if the image exists before deleting it
- [ ] Add github actions to build the image and check everything work
    - [ ] Add tests to check everything is installed
    - [ ] Add github action to build the image and run the tests
- [ ] Add a menu with options
- [ ] Add commands wrapper (like exegol)
- [ ] Add log file