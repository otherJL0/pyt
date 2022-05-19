from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


@app.command()
def init(directory: Optional[str] = typer.Argument(None)):
    git_dir: Path = Path.cwd()
    if directory:
        git_dir /= directory
    git_dir /= ".git"
    layout = ("objects", "refs", "hooks", "info")

    try:
        for dir in layout:
            (git_dir / dir).mkdir(parents=True, exist_ok=False)
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


@app.command()
def add():
    print("pyt add")


@app.command()
def commit():
    print("pyt commit")
