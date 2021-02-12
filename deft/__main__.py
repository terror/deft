import typer
import time
from client import Client

app = typer.Typer()
client = Client()


@app.command()
def hello(name: str):
    typer.echo("Hello {}".format(name))


@app.command()
def bye(name: str):
    typer.echo("Bye! {}".format(name))


@app.command()
def run():
    while True:
        time.sleep(10)
        print("hello world!")


if __name__ == "__main__":
    app()
