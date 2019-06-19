# Collection Demo

This project is for showcasing distributing modules and roles via collections in Ansible 2.8.
To run this demo you need to:

1. Install the latest version of mazer: `pip install mazer`.
2. Install or upgrade to the latest version of Ansible
3. Download the collection from galaxy: `mazer install newswangerd.collection_demo`

Now you can either

- Execute the `real_facts` module using `ansible localhost -m newswangerd.collection_demo.real_facts`

or

- Download the `collections_in_playbooks.yaml` playbook from this repository.
- Run it using `ansible-playbook collections_in_playbooks.yaml`

If that sounds like too much work, there's also a pre recorded demo using this
collection [available on YouTube](https://www.youtube.com/watch?v=d792W44I5KM).
