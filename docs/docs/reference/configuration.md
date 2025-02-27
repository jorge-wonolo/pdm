# Configurations

[pdm-config]: ../reference/cli.md#config

## Color Theme

The default theme used by PDM is as follows:

| Key       | Default Style                                                |
| --------- | ------------------------------------------------------------ |
| `primary` | <span style="color:cyan">cyan</span>                         |
| `success` | <span style="color:green">green</span>                       |
| `warning` | <span style="color:yellow">yellow</span>                     |
| `error`   | <span style="color:red">red</span>                           |
| `info`    | <span style="color:blue">blue</span>                         |
| `req`     | <span style="color:green;font-weight:bold">bold green</span> |

You can change the theme colors with [`pdm config`][pdm-config] command. For example, to change the `primary` color to `magenta`:

```bash
pdm config theme.primary magenta
```

Or use a hex color code:

```bash
pdm config theme.success '#51c7bd'
```

## Available Configurations

The following configuration items can be retrieved and modified by [`pdm config`][pdm-config] command.

| Config Item                       | Description                                                               | Default Value                                                         | Available in Project | Env var                   |
| --------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------- | -------------------- | ------------------------- |
| `build_isolation`                 | Isolate the build environment from the project environment                | Yes                                                                   | True                 | `PDM_BUILD_ISOLATION`     |
| `cache_dir`                       | The root directory of cached files                                        | The default cache location on OS                                      | No                   |                           |
| `check_update`                    | Check if there is any newer version available                             | True                                                                  | No                   | `PDM_CHECK_UPDATE`        |
| `global_project.fallback`         | Use the global project implicitly if no local project is found            | `False`                                                               | No                   |                           |
| `global_project.fallback_verbose` | If True show message when global project is used implicitly               | `True`                                                                | No                   |                           |
| `global_project.path`             | The path to the global project                                            | `<default config location on OS>/global-project`                      | No                   |                           |
| `global_project.user_site`        | Whether to install to user site                                           | `False`                                                               | No                   |                           |
| `install.cache`                   | Enable caching of wheel installations                                     | False                                                                 | Yes                  |                           |
| `install.cache_method`            | Specify how to create links to the caches(`symlink` or `pth`)             | `symlink`                                                             | Yes                  |                           |
| `install.parallel`                | Whether to perform installation and uninstallation in parallel            | `True`                                                                | Yes                  | `PDM_PARALLEL_INSTALL`    |
| `project_max_depth`               | The max depth to search for a project through the parents                 | 5                                                                     | No                   | `PDM_PROJECT_MAX_DEPTH`   |
| `python.use_pyenv`                | Use the pyenv interpreter                                                 | `True`                                                                | Yes                  |                           |
| `python.use_venv`                 | Use virtual environments when available                                   | `True`                                                                | Yes                  | `PDM_USE_VENV`            |
| `pypi.url`                        | The URL of PyPI mirror                                                    | `https://pypi.org/simple`                                             | Yes                  | `PDM_PYPI_URL`            |
| `pypi.username`                   | The username to access PyPI                                               |                                                                       | Yes                  | `PDM_PYPI_USERNAME`       |
| `pypi.password`                   | The password to access PyPI                                               |                                                                       | Yes                  | `PDM_PYPI_PASSWORD`       |
| `pypi.ignore_stored_index`        | Ignore the configured indexes                                             | `False`                                                               | Yes                  | `PDM_IGNORE_STORED_INDEX` |
| `pypi.ca_certs`                   | Path to a PEM-encoded CA cert bundle (used for server cert verification)  | The CA certificates from [certifi](https://pypi.org/project/certifi/) | No                   |                           |
| `pypi.client_cert`                | Path to a PEM-encoded client cert and optional key                        |                                                                       | No                   |                           |
| `pypi.client_key`                 | Path to a PEM-encoded client cert private key, if not in pypi.client_cert |                                                                       | No                   |                           |
| `pypi.verify_ssl`                 | Verify SSL certificate when query PyPI                                    | `True`                                                                | Yes                  |                           |
| `pypi.json_api`                   | Consult PyPI's JSON API for package metadata                              | `False`                                                               | Yes                  | `PDM_PYPI_JSON_API`       |
| `strategy.save`                   | Specify how to save versions when a package is added                      | `minimum`(can be: `exact`, `wildcard`, `minimum`, `compatible`)       | Yes                  |                           |
| `strategy.update`                 | The default strategy for updating packages                                | `reuse`(can be : `eager`)                                             | Yes                  |                           |
| `strategy.resolve_max_rounds`     | Specify the max rounds of resolution process                              | 10000                                                                 | Yes                  | `PDM_RESOLVE_MAX_ROUNDS`  |
| `venv.location`                   | Parent directory for virtualenvs                                          | `<default data location on OS>/venvs`                                 | No                   |                           |
| `venv.backend`                    | Default backend to create virtualenv                                      | `virtualenv`                                                          | Yes                  | `PDM_VENV_BACKEND`        |
| `venv.prompt`                     | Formatted string to be displayed in the prompt when virtualenv is active  | `{project_name}-{python_version}`                                     | Yes                  | `PDM_VENV_PROMPT`         |
| `venv.in_project`                 | Create virtualenv in `.venv` under project root                           | `False`                                                               | Yes                  | `PDM_VENV_IN_PROJECT`     |
| `venv.with_pip`                   | Install pip when creating a new venv                                      | `False`                                                               | Yes                  | `PDM_VENV_WITH_PIP`       |

_If the corresponding env var is set, the value will take precedence over what is saved in the config file._
