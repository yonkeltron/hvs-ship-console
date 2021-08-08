from pyinfra.operations import git, server

server.shell(
    name='Install and set up Volta',
    commands=[
        'curl https://get.volta.sh | bash',
        'volta setup'
    ]
)

git.repo(
    name='Clone hvs-ship-console',
    src='',
    dest='',
    branch='main'
)
