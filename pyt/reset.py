import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def reset() -> None:
    print("pyt reset")
