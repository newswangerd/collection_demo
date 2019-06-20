## Playbook examples

This first example runs a module within the collection:


```
- name: Run a module from inside a collection
  hosts: localhost
  tasks:
    - name: Gather some real Facts.
      newswangerd.collection_demo.real_facts:
        name: Richard Stallman
      register: testout
    - debug:
        msg: "{{ testout }}"
```

This example uses the `collections` keyword:

```
- name: Run a module from inside a collection using the collections keyword
  hosts: localhost
  collections:
    - newswangerd.collection_demo
  tasks:
    - name: Gather some real Facts.
      real_facts:
        name: Richard Stallman
      register: testout
    - debug:
        msg: "{{ testout }}"
```
