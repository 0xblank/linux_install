#   Linux install

<div align="center">
    <br>
    <img alt="Python3.9" src="https://img.shields.io/badge/Python-3.9+-informational">
    <img alt="current version" src="https://img.shields.io/badge/debian-supported-success">
    <img alt="current version" src="https://img.shields.io/badge/ubuntu-supported-success">
    </br>
</div>

Simple scripts I decided to write to automate my linux installations after (way) too many of them done manually.

:warning: **This tool only works for debian based distibutions** :warning:

> The docker and the build things are just here for testing purposes.

This projet was inspired by [exegol](https://github.com/ThePorgs/Exegol). Awesome project, go check it out !

##  How to use

```
# apt install git
$ git clone https://github.com/0xblank/linux_install.git
# ./install/entrypoint.sh
```

> The script must be run as with root privileges so it can install packages and everything

You can edit the packages and git_repositories files to install your own packages and git repositories.

##  How to contribute

Create an issue or a pull request and I will check it out.

##  TO DO list

### Install

- [ ] Support Ubuntu
- [ ] Add git repositories
- [ ] Add debian/ubuntu repositories for
    - [ ] codium
    - [ ] lspci
    - [ ] poetry
- [ ] Put config files in the right spots
    - [ ] i3 or sway
    - [ ] terminator
    - [ ] zshrc
- [ ] Make custom installs
    - [ ] oh my zsh
        - [ ] zinit
        - [ ] plugins from zsh_plugin file
    - [ ] Docker
    - [ ] Starship
    - [ ] Vagrant
    - [ ] Exegol
    - [ ] Burp
    - [ ] (maybe) VM ware workstation pro
    - [ ] (maybe) virtualbox
    - [ ] Vagrant
    - [ ] Obsidian
    - [ ] Helix
- [ ] Generate rsa keys pairs
    - [ ] github
    - [ ] gitlab
    - [ ] servers

### Ease of use

- [ ] Add commands wrapper with multiple options (like exegol)
    - [ ] (maybe) create multiple premade profiles
    - [ ] (maybe) add fully customisable install (chose of packets, repos, shell ...)
- [ ] Add log file

### Testing

- [ ] Check if the image exists before deleting it
- [ ] Add github actions to build the image and check everything work
    - [ ] Add tests to check everything is installed
    - [ ] Add github action to build the image and run the tests
- [ ] Add a menu with options

### Other

- [ ] Add other distribution support (like arch)
