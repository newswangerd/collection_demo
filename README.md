# What is a collection?

A collection is a distribution format for delivering all types of Ansible Content.

The standard format for a collection looks something like this:

```
demo/
├── README.md
├── galaxy.yml
├── plugins
│   └── modules
│       └── real_facts.py
└── roles
    └── factoid
        ├── README.md
        ├── meta
        │   └── main.yaml
        └── tasks
            └── main.yml
```

It includes a `galaxy.yml` file for defining the collections name, version, tags, license and other meta data as well as
directories for roles and plugins. The roles directory contains a list of traditional roles and the plugins directory can
contain subdirectories for all of the Ansible plugin types such as modules, inventory, callback, connection plugins and more.

# How do I build a collection?

Collections are currently built using [mazer](https://github.com/ansible/mazer/). To build this collection:

```
$ cd demo
$ mazer build
```

This will create a releases directory with tarballs of each release. These tarballs can be uploaded and distributed
through galaxy.

```
├── releases
│   └── newswangerd-demo-1.0.1.tar.gz
```

# How do I use a collection?

Collections are stored in `~/.ansible/collections/ansible_collections`. You can either place a collection here
manually or you can use `mazer install namespace.collection_name` to download an existing collection from Galaxy
and have it install automatically.

Collections in playbooks can be used like so:

```
################################################################################
- name: Run a module from inside a collection
  hosts: localhost
  tasks:
    - name: Gather some real Facts.
      newswangerd.demo.real_facts:
        name: Richard Stallman
      register: testout
    - debug:
        msg: "{{ testout }}"

################################################################################
- name: Run a module from inside a collection using the collections keyword
  hosts: localhost
  collections:
    - newswangerd.demo
  tasks:
    - name: Gather some real Facts.
      real_facts:
        name: Richard Stallman
      register: testout
    - debug:
        msg: "{{ testout }}"

################################################################################
- name: Run a role from inside of a collection
  hosts: localhost
  roles:
    - "newswangerd.demo.factoid"
```
