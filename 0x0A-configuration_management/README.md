# 0x0A. Configuration management
##### `DevOps` `SysAdmin` `Scripting` `CI/CD`

## Resources
**Read or watch:**
* [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
* [Puppet resource type: file (check “Resource types” for all manifest types in the left menu)](https://www.puppet.com/docs/puppet/5.5/types/file.html)
* [Puppet’s Declarative Language: Modeling Instead of Scripting](https://www.puppet.com/blog)
* [Puppet lint](http://puppet-lint.com/)
* [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)

## Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

### Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```

### Install puppet-lint
```
$ gem install puppet-lint
```

## Tasks
0. Create a file

Using Puppet, create a file in `/tmp`.

Requirements:

* File path is `/tmp/school`
* File permission is `0744`
* File owner is `www-data`
* File group is `www-data`
* File contains `I love Puppet`

1. Install a package

Using Puppet, install `flask` from `pip3`.

Requirements:

* Install `flask`
* Version must be `2.1.0`

2. Execute a command

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

* Must use the `exec` Puppet resource
* Must use `pkill`

Example:

Terminal #0 - starting my process
