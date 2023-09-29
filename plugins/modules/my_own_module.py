#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

version_added: "1.0.0"

description: This module creates a text file with specified content.

options:
    path:
        description: The path where the file should be created.
        required: true
        type: str
    content:
        description: The content to be added to the file.
        required: true
        type: str

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Create a file with specified content
- name: Create a file
  my_namespace.my_collection.my_test:
    path: /path/to/file.txt
    content: 'Hello, World!'
'''

RETURN = r'''
path:
    description: The path of the file that was created or checked.
    type: str
    returned: always
message:
    description: The outcome message.
    type: str
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule
import os

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    file_path = module.params['path']
    file_content = module.params['content']

    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(file_content)
        result['changed'] = True
        result['message'] = f"File {file_path} has been created."
    else:
        result['message'] = f"File {file_path} already exists."

    result['path'] = file_path

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
