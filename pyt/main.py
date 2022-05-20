import typer

import pyt.add as add
import pyt.commit as commit
import pyt.init as init
import pyt.pull as pull
import pyt.push as push
import pyt.reset as reset
import pyt.show as show
import pyt.status as status

app = typer.Typer()
app.add_typer(add.app, name="add")
app.add_typer(commit.app, name="commit")
app.add_typer(init.app, name="init")
app.add_typer(pull.app, name="pull")
app.add_typer(push.app, name="push")
app.add_typer(reset.app, name="reset")
app.add_typer(show.app, name="show")
app.add_typer(status.app, name="status")
