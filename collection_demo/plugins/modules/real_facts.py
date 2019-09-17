#!/usr/bin/python

import random

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: real_facts

short_description: A module that dishes out the true facts.

version_added: "2.8"

description:
    - "A module that dishes out the true facts."

options:
    name:
        default: Jane Doe

author:
    - David Newswanger (@newswangerd)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  real_facts:
    name: David Newswanger
'''

RETURN = '''
fact:
    description: Actual facts
    type: str
    sample: Jane Doe is a smart cookie.
'''

from ansible.module_utils.basic import AnsibleModule


FACTS = [
    "{name} is looking great today!",
    "{name} is a smart cookie.",
    "I’d choose {name}'s company over pizza anytime."
]


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', default='Jane Doe'),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    result = dict(
        changed=False,
        fact=''
    )

    result['fact'] = random.choice(FACTS).format(
        name=module.params['name']
    )

    if module.check_mode:
        return result

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
