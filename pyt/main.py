import typer

import pyt.init as init

app = typer.Typer()
app.add_typer(init.app, name="init")
