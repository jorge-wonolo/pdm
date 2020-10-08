import os
import subprocess
import sys

from build import ProjectBuilder
from build.env import IsolatedEnvironment

from pdm.exceptions import BuildError
from pdm.iostream import stream
from pdm.pep517.base import Builder

_SETUPTOOLS_SHIM = (
    "import sys, setuptools, tokenize; sys.argv[0] = {0!r}; __file__={0!r};"
    "f=getattr(tokenize, 'open', open)(__file__);"
    "code=f.read().replace('\\r\\n', '\\n');"
    "f.close();"
    "exec(compile(code, __file__, 'exec'))"
)


def log_subprocessor(cmd, cwd=None, extra_environ=None):
    env = os.environ.copy()
    if extra_environ:
        env.update(extra_environ)
    capture_output = bool(stream.logger)
    proc = subprocess.run(cmd, cwd=cwd, env=env, capture_output=capture_output)
    if capture_output:
        stream.logger.debug(proc.stdout.decode("utf-8"))
    if proc.returncode:
        stream.logger.debug(proc.stderr.decode("utf-8"))
        raise BuildError(f"Call command {cmd} return non-zero status.")


def build_wheel(src_dir: str, out_dir: str) -> str:
    """Build wheel and return the full path of the artifact."""
    builder = ProjectBuilder(srcdir=src_dir)
    stream.echo("Building wheel...")
    with IsolatedEnvironment.for_current() as env, builder.hook.subprocess_runner(
        log_subprocessor
    ):
        env.install(builder.build_dependencies)
        filename = builder.hook.build_wheel(out_dir)
    stream.echo(f"Built {filename}")
    return os.path.join(out_dir, filename)


def build_sdist(src_dir: str, out_dir: str) -> str:
    """Build sdist and return the full path of the artifact."""
    builder = ProjectBuilder(srcdir=src_dir)
    stream.echo("Building sdist...")
    with IsolatedEnvironment.for_current() as env, builder.hook.subprocess_runner(
        log_subprocessor
    ):
        env.install(builder.build_dependencies)
        filename = builder.hook.build_sdist(out_dir)
    stream.echo(f"Built {filename}")
    return os.path.join(out_dir, filename)


def _find_egg_info(directory: str) -> str:
    filename = next(
        (f for f in os.listdir(directory) if f.endswith(".egg-info")),
        None,
    )
    if not filename:
        raise BuildError("No egg info is generated.")
    return filename


def build_egg_info(src_dir: str, out_dir: str) -> str:
    # Ignore destination since editable builds should be build locally
    builder = Builder(src_dir)
    setup_py_path = builder.ensure_setup_py().as_posix()
    with IsolatedEnvironment.for_current() as env:
        env.install(["setuptools"])
        args = [sys.executable, "-c", _SETUPTOOLS_SHIM.format(setup_py_path)]
        args.extend(["egg_info", "--egg-base", out_dir])
        stream.echo("Building egg info...")
        log_subprocessor(args, cwd=src_dir)
        filename = _find_egg_info(out_dir)
    stream.echo(f"Built {filename}")
    return os.path.join(out_dir, filename)