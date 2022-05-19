from pathlib import Path
from typing import Optional

import typer

app = typer.Typer()


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
