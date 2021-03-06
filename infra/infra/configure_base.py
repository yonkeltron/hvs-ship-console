from pyinfra.operations import apt, files, server

apt.key(
    name='Add Tailscale GPG key',
    src='https://pkgs.tailscale.com/stable/debian/buster.gpg'
)

apt.repo(
    name='Add Tailscale apt repo',
    src='deb https://pkgs.tailscale.com/stable/debian buster main'
)

apt.update(name='Update available package lists')
apt.upgrade(name='Upgrade all system packages')

apt.packages(
    name='Ensure that needed packages are installed',
    packages=['emacs-nox', 'git', 'htop', 'mosh', 'sudo', 'tailscale', 'tmux'],
    latest=True,
)

with open('/home/yonkeltron/.ssh/id_ed25519.pub', 'r') as key_file:
    public_ssh_key = key_file.read()

server.user(
    name='Create yonkeltron user',
    user='yonkeltron',
    present=True,
    ensure_home=True,
    public_keys=public_ssh_key,
    shell="/usr/bin/bash"
)

files.directory(
    name='Create AITH data dir',
    path='/opt/aith',
    present=True,
    user='yonkeltron',
    group='yonkeltron',
    recursive=True,
)

files.put(
    name='Upload Caddy binary',
    src='caddy_linux_amd64',
    dest='/usr/local/bin/caddy',
    mode='u=rwx,g=rx,o=rx'
)
