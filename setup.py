# Copyright 2017 Michael R. Shannon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""setup.py: setuptools control."""


import re
from setuptools import setup


with open('cfgtool/cfgtool.py') as f:
    version = re.search("^__version__\s*=\s*'(.*)'", f.read(), re.M).group(1)
    print(version)


with open('README.md', 'r') as f:
    long_description = f.read()


setup(
        name = 'cfgtool',
        packages = ['cfgtool'],
        entry_points = {
            'console_scripts': ['cfgtool = cfgtool.cfgtool:main']
            },
        version = version,
        description = (
            'Command line program to create/modify/read configuration files'),
        long_description = long_description,
        author = 'Michael R. Shannon',
        author_email = 'mrshannon.aerospace@gmail.com',
        url = 'https://github.com/mrshannon/python-cfgtool'
        )
