# This file will be executed trying to execute this dir (entrypoint)

import deps  # Import all content using an object
from deps import DepsClass, deps_func  # Import specific content from the file

print(deps.deps_variable)  # 10

object = DepsClass()

object.func()  # DepsClass->func execution

deps_func()  # deps_func execution
