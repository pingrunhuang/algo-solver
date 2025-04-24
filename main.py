from importlib import import_module
import click


@click.command()
@click.option("--module-name")
def main(module_name:str):
    print(module_name)
    mde = import_module(module_name)
    sol = mde.Solution()
    sol.run()


if __name__ == "__main__":
    main()