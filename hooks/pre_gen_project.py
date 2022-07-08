import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_name = '{{ cookiecutter.project_name }}'
package_name = '{{ cookiecutter.package_name }}'

msg = []

if not re.match(MODULE_REGEX, package_name):
    msg.append("'%s' is not a valid Python module name" % package_name)

if " " in project_name:
    msg.append("'%s' is not a valid project name because it contains spaces" % package_name)

if msg:
    print()
    print("#########################################################")
    print("The following errors were detected in the project:")
    for i in msg:
        print("-", i)
    print("#########################################################")
    print()
    # exits with status 1 to indicate failure
    sys.exit(1)
