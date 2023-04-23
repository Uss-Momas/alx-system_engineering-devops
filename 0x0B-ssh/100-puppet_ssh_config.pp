# puppet manifest to create/modify content of ssh client config
file {'ssh_school':
ensure  => present,
path    => '/home/ussumane/.ssh/config',
content => 'Host 34.202.159.196
IdentityFile ~/.ssh/school
PasswordAuthentication no'
}
