import os
import uuid
import click
from kervi_cli.scripts.template_engine import SuperFormatter
import kervi_cli

@click.group()
def create():
    pass

@create.command()
@click.argument('app_id',"Id of application, used in code to identify app")
@click.argument('app_name','Name of app, used at title in UI')
@click.option('--platform', default=None, help='RPI')
def application(app_name, app_id, platform):
    click.echo('create app:'+app_name)
    template_engine = SuperFormatter()

    cli_path = os.path.dirname(kervi_cli.__file__)
    template_path = os.path.join(cli_path, "templates/")

    app_template = open(template_path+"app_tmpl.py", 'r').read()
    app_file_content = template_engine.format(
        app_template,
        id=app_id,
        name=app_name,
        log="kervi.log",
        base_port=9500,
        websocket_port=9000,
        ui_port=80,
        secret=uuid.uuid4()
    )

    if not os.path.exists(app_id+".py"):
        app_file = open(app_id+".py", "w")
        app_file.write(app_file_content)
        app_file.close()

    if not os.path.exists("sensors"):
        os.makedirs("sensors")
        open("sensors/__init__.py", 'a').close()

    if not os.path.exists("controllers"):
        os.makedirs("controllers")
        open("controllers/__init__.py", 'a').close()

    if not os.path.exists("dashboards"):
        os.makedirs("dashboards")
        open("dashboards/__init__.py", 'a').close()
