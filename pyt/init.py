from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


@dataclass
class GitConfigSegment:
    """Custom dataclass provides more control over configparser module"""

    segment_name: str = ""

    def __post_init__(self) -> None:
        """If a segment name is provided, prepend with a space"""
        if self.segment_name:
            self.segment_name = f' "{self.segment_name}"'

    def __str__(self) -> str:
        """Return formatted segment, all in lowercase"""
        header = f"[{self.__class__.__name__}{self.segment_name}]"
        fields = asdict(self)
        del fields["segment_name"]
        body = "\n".join(f"\t{name} = {value}" for name, value in fields.items())
        return f"{header}\n{body}".lower()


@dataclass
class Core(GitConfigSegment):
    repositoryformatversion: int = 0
    filemode: bool = True
    bare: bool = False
    logallrefupdates: bool = True


def generate_config(git_dir: Path) -> None:
    config = Core()
    with (git_dir / "config").open("w", encoding="utf-8") as gitconfig:
        gitconfig.write(str(config))


@app.callback(invoke_without_command=True)
def init(directory: Optional[str] = typer.Argument(None)):
    git_dir: Path = Path.cwd()
    if directory:
        git_dir /= directory
    git_dir /= ".git"
    layout = ("objects", "refs", "hooks", "info")

    try:
        for dir in layout:
            (git_dir / dir).mkdir(parents=True, exist_ok=False)
        generate_config(git_dir)
        message = typer.style(
            f"Initialized empty Pyt repository in {typer.style(git_dir, underline=True)}",
            fg=typer.colors.GREEN,
        )
    except FileExistsError:
        for dir in layout:
            (git_dir / dir).mkdir(parents=True, exist_ok=True)
        message = typer.style(
            f"Reinitialized existing Pyt repository in {typer.style(git_dir, underline=True)}",
            fg=typer.colors.YELLOW,
        )
    typer.echo(message)
