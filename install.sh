#/usr/bin/env bash


if [ ! -d "/usr/local/var/kanban_app" ]; then
  mkdir "/usr/local/var/kanban_app"
fi
cp -R ./* /usr/local/var/kanban_app/.

if [ ! -d "$HOME/bin" ]; then
  mkdir "$HOME/bin"
fi

ln -fs /usr/local/var/kanban_app/kanban.py $HOME/bin/kb

echo "KAnBan Application Installed - you will need to add ~/bin to your path."
