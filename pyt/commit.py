import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def commit() -> None:
    print("pyt commit")
