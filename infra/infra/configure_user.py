from pyinfra import host
from pyinfra.facts import files
from pyinfra.operations import git, server

if host.get_fact(files.Directory, '/home/yonkeltron/.volta'):
    server.shell(
        name='Install and set up Volta',
        commands=[
            'curl https://get.volta.sh | bash',
            'volta setup'
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

git.repo(
    name='Clone hvs-ship-console',
    src='https://github.com/yonkeltron/hvs-ship-console.git',
    dest='/opt/aith/hvs-ship-console',
    branch='main'
)
