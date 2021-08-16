from pyinfra import host
from pyinfra.facts import files
from pyinfra.operations import files, git, server

if not host.get_fact(files.Directory, '/home/yonkeltron/.volta'):
    server.shell(
        name='Install and set up Volta',
        commands=[
            'curl https://get.volta.sh | bash',
            '/home/yonkeltron/.volta/bin/volta setup'
        ]
    )

git.config(
    name='Set git name',
    key='user.name',
    value='Jonathan E. Magen'
)

git.config(
    name='Set git email',
    key='user.email',
    value='yonkeltron@gmail.com'
)

files.directory(
    name='Create AITH data dir',
    path='/opt/aith/hvs-ship-console',
    present=False,
)

files.put(
    name='Upload Caddyfile',
    src='Caddyfile',
    dest='Caddyfile'
)
