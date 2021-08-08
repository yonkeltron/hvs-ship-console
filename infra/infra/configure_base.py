from pyinfra.operations import apt, server

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
    packages=['emacs-nox', 'htop', 'mosh', 'sudo', 'tailscale', 'tmux'],
    latest=True,
)

with open('~/.ssh/id_rsa.pub', 'r') as key_file:
    public_ssh_key = key_file.read()

server.user(
    name='Create yonkeltron user',
    user='yonkeltron',
    present=True,
    ensure_home=True,
    public_keys=public_ssh_key
)
