import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def status() -> None:
    print("pyt status")
