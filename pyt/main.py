import typer

app = typer.Typer()


@app.command()
def init():
    print("pyt init")


@app.command()
def add():
    print("pyt add")


@app.command()
def commit():
    print("pyt commit")
