import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def show() -> None:
    print("pyt show")
