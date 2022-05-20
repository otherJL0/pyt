from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


@dataclass
class PytConfigSegment:
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
class Core(PytConfigSegment):
    repositoryformatversion: int = 0
    filemode: bool = True
    bare: bool = False
    logallrefupdates: bool = True


@app.callback(invoke_without_command=True)
def init(directory: Optional[str] = typer.Argument(None)):
    pyt_dir: Path = Path.cwd()
    if directory:
        pyt_dir /= directory
    pyt_dir /= ".pyt"

    # Contents of .pyt directory
    subdirectories = ("objects", "refs", "hooks", "info")
    files: dict[str, str] = {
        "config": str(Core()),
        "description": "Unnamed repository; edit this file 'description' to name the repository.",
        "HEAD": "ref: refs/heads/master",
    }

    try:
        for dir in subdirectories:
            (pyt_dir / dir).mkdir(parents=True, exist_ok=False)
        for filename, contents in files.items():
            with (pyt_dir / filename).open("w", encoding="utf-8") as f:
                f.write(contents)

        message = typer.style(
            f"Initialized empty Pyt repository in {typer.style(pyt_dir, underline=True)}",
            fg=typer.colors.GREEN,
        )
    except FileExistsError:
        for dir in subdirectories:
            (pyt_dir / dir).mkdir(parents=True, exist_ok=True)
        message = typer.style(
            f"Reinitialized existing Pyt repository in {typer.style(pyt_dir, underline=True)}",
            fg=typer.colors.YELLOW,
        )
    typer.echo(message)
