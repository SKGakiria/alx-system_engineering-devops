# Puppet script to fix typos in the php settings file

exec { 'fix_typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
