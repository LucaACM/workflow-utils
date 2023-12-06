# workflow-utils
python scripts to automate tedious or repetitive tasks

git para abrir repos por nombre de proyecto

recomendacion, crear un alias o empaquetarlo

command format

``` bash
$ python3 script_path service arg1 arg2 arg3... -flag1 -flag2 -flag3
```

## services

* git: abre los repositorios en el navegador por defecto, flag -pr abre directamente la ventana de los pr filtrados por los creados por el usuario

* log: realiza un docker logs --follow por cada servicio pasado por args, cada uno en una pestaña nueva de iterm2

* code: abre en visual studio los repo de los proyectos pasados por args

* ww: modifica docker compose para levantar en watch mode los servicios que se le indiquen en los args, y aquellos que no esten los modifica igualmente para que se levanten con npm run start