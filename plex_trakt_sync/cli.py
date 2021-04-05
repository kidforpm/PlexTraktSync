import click
from plex_trakt_sync.clear_trakt_collections import clear_trakt_collections
from plex_trakt_sync.commands.sync import sync


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """
    Plex-Trakt-Sync is a two-way-sync between trakt.tv and Plex Media Server
    """
    if not ctx.invoked_subcommand:
        sync()


@click.command()
@click.option('--confirm', is_flag=True, help='Confirm the dangerous action')
def clear_collections(confirm):
    """
    Clear Movies and Shows collections in Trakt
    """

    if not confirm:
        click.echo('You need to pass --confirm option to proceed')
        return
    clear_trakt_collections()


cli.add_command(sync)
cli.add_command(clear_collections)