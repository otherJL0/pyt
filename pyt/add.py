import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def add() -> None:
    print("pyt add")
