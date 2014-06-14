#!/bin/bash
source="./*"
echo -n "Enter full path to directory for JoomlaDevTool (Enter if /opt/joomladevtool/): "
read dest
if [ -z $dest ] ; then
  dest='/opt/joomladevtool/'
fi
if [ ! -d $dest ] ; then
  mkdir "$dest"
fi
cp -rp $source $dest
cd $dest
chmod -R 775 $dest
rm 'install.sh'
if [[ -f /usr/bin/python ]]; then
	pypath='python'
fi
if [[ -f /usr/bin/python2.7 ]]; then
	pypath='python2.7'
fi
if [[ -f /usr/bin/python3 ]]; then
	pypath='python3'
fi
cd /usr/bin/
touch joomdevtool
echo '#!/bin/bash
parameters=$@
'$pypath $dest'/main.py $parameters
exit 0' > joomdevtool
chmod +x joomdevtool