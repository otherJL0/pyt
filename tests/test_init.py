import subprocess
from pathlib import Path


def capture(command: tuple[str, ...]) -> tuple[bytes, bytes, int]:
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    return out, err, proc.returncode


def test_pyt_init_new_repo(tmp_path: Path):
    command = ("pyt", "init", str(tmp_path))
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert (
        out.decode().strip() == f"Initialized empty Pyt repository in {tmp_path}/.pyt/"
    )


def test_pyt_init_existing_repo(tmp_path: Path):
    command = ("pyt", "init", str(tmp_path))
    capture(command)
    out, _, exitcode = capture(command)
    assert exitcode == 0
    assert (
        out.decode().strip()
        == f"Reinitialized existing Pyt repository in {tmp_path}/.pyt/"
    )


def test_generate_identical_files(tmp_path: Path):
    for tool in ("git", "pyt"):
        _, _, exitcode = capture((tool, "init", str(tmp_path)))
        assert exitcode == 0

    pyt_dir = set(
        item.relative_to(tmp_path / ".pyt") for item in (tmp_path / ".pyt").iterdir()
    )
    git_dir = set(
        item.relative_to(tmp_path / ".git") for item in (tmp_path / ".git").iterdir()
    )
    assert pyt_dir == git_dir
