# project
a simple pattern for managing configs and paths within a project

## use
1. install project
2. copy the config folder from `project/config` to your own project or...
2a. make a folder in your project called config
2b. make a file in `config/__init__.py`

paste the following code:
```
import os
from functools import partial
from project import root, get, put, env, var


root = partial(root, os.path.abspath(__file__))
get = partial(get, root=root)
put = partial(put, root=root)
env = partial(env, get=get, root=root)
```



Now, throughout your project you can use it like this:

```
>>> from <my_project> import config

>>> # returns dictionary of config/config.yaml
>>> config.get()
{'setting': False}

>>> # returns path of where the file was saved
>>> config.put(data={'abc': 123}, path=config.root('config', 'other_configs.yaml'))
'/repos/project/project/config/other_configs.yaml'

>>> # returns dictionary of config/other_configs.yaml
>>> config.get('other_configs')
{'abc': 123}

>>> # returns string of root directory of your project
>>> config.root()
'/repos/project/project'

>>> # returns string of root directory of your project joined to this suffix
>>> config.root('lib', '__init__.py')
'/repos/project/project/lib/__init__.py'
```
