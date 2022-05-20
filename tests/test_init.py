import subprocess
from pathlib import Path


def capture(command: tuple[str, ...]) -> tuple[bytes, bytes, int]:
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_git_init_new_repo(tmp_path: Path):
    command = ("git", "init", str(tmp_path))
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert (
        out.decode().strip() == f"Initialized empty Git repository in {tmp_path}/.git/"
    )


def test_pyt_init_new_repo(tmp_path: Path):
    command = ("pyt", "init", str(tmp_path))
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert (
        out.decode().strip() == f"Initialized empty Pyt repository in {tmp_path}/.pyt/"
    )
