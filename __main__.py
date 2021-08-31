# -*- coding: UTF-8 -*-
import pdb
import sys
import os
import fileinput

pythonName = "python"
pipName = "pip"

if sys.platform == "darwin":
	pythonName = "python3"
	pipName = "pip3"

#####
version = '2.0'
#####

text_index = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Home</title>
</head>
<body>
  {% load static %}
  {{ saludo }}
  <script src="{% static 'js/index.js' %}"></script>
</body>
</html>
'''


def add_after(filename, old_line, new_line, esReemplazo=False):
    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
        for line in f:
            if old_line in line:
                if esReemplazo:
                    print(new_line)
                else:
                    print(line +  new_line, end='\n')
            else:
                print(line, end='')


def create_app(project, app):
	# Genera Aplicacion
	string = '... GENERANDO APLICACION DE NOMBRE "' + app + '" AL PROYECTO "' + project + '"';		os.system('echo ' + string)
	os.chdir(project)
	os.system(f'{pythonName} manage.py startapp {app}')
	
	# Implementa Configuraciones
	string = '... IMPLEMENTANDO CONFIGURACIONES LOCALES AL PROYECTO »» "' + project + '"';			os.system('echo ' + string)
	add_after(f'{project}/settings.py', 'INSTALLED_APPS', f"    '{app}',")
	add_after(f'{project}/settings.py', f"LANGUAGE_CODE = 'en-us'", f"LANGUAGE_CODE = 'es'", True)
	add_after(f'{project}/settings.py', f"TIME_ZONE = 'UTC'", f"TIME_ZONE = 'America/Santiago'", True)
	add_after(f'{project}/urls.py', 'from django.urls', 'from django.urls import include')
	add_after(
		f'{project}/urls.py',
		'urlpatterns = [',
		f"    path('', include('{app}.urls')),")
	
	# Implementa Plantillas
	string = '... IMPLEMENTANDO PLANTILLAS A LA APLICACION »» "' + app + '"';						os.system('echo ' + string)
	os.system(f'cp -R ../crear/templates {app}/templates')
	os.system(f'cp -R ../crear/static {app}/static')
	os.system(f'cp ../crear/views.py {app}/views.py')
	os.system(f'cp ../crear/auth.py {app}/auth.py')
	os.system(f'cp ../crear/decorators.py {app}/decorators.py')
	os.system(f'cp ../crear/models.py {app}/models.py')
	os.system(f'cp ../crear/urls.py {app}/urls.py')
	os.system(f'cp ../crear/admin.py {app}/admin.py')
	os.system(f'cp ../crear/gitignore .gitignore')


	# Implementa Dependencias del proyecto base
	string = '.';																					os.system('echo ' + string)
	string = '..';																					os.system('echo ' + string)	
	string = '... INSTALANDO DEPENDENCIAS EN EL AMBIENTE AL PROYECTO  »»  "' + project + '"';		os.system('echo ' + string)
	string = "###############################################################################";		os.system('echo ' + string)
	os.system(f'{pipName} install bcrypt --quiet')
	string = "###############################################################################";		os.system('echo ' + string)


	# # Ejecuta Makemigrations
	# string = '.';																					os.system('echo ' + string)
	# string = '..';																					os.system('echo ' + string)	
	# string = '... EJECUTANDO MAKEMIGRATIONS AL PROYECTO »» "' + project + '"';						os.system('echo ' + string)
	# string = "###############################################################################";		os.system('echo ' + string)
	# os.system(f'{pythonName} manage.py makemigrations')
	# string = "###############################################################################";		os.system('echo ' + string)

	# # Ejecuta Migrate
	# string = '.';																					os.system('echo ' + string)
	# string = '..';																					os.system('echo ' + string)
	# string = '... EJECUTANDO MIGRATE AL PROYECTO »» "' + project + '"' ;							os.system('echo ' + string)
	# string = "###############################################################################";		os.system('echo ' + string)
	# os.system(f'{pythonName} manage.py migrate')
	# string = "###############################################################################";		os.system('echo ' + string)
	
	# fin
	string = '.';																					os.system('echo ' + string)
	string = '..';																					os.system('echo ' + string)
	string = '...';																					os.system('echo ' + string)
	string = "╔═════════════════════════════════════════════╗";										os.system('echo ' + string)
	string = "║       PROYECTO GENERADO CORRECTAMENTE       ║";										os.system('echo ' + string)
	string = "╚═════════════════════════════════════════════╝";										os.system('echo ' + string)
	string = '...';																					os.system('echo ' + string)
	string = '..';																					os.system('echo ' + string) 
	string = '.';																					os.system('echo ' + string)
	
def main():
	if len(sys.argv) < 3:
		os.system('clear')
		string = "╔═════════════════════════════════════════════╗"; 								os.system('echo ' + string)
		string = "║     GENERADOR DE PROYECTOS DJANGO  v" + version + "     ║";						os.system('echo ' + string)
		string = "╠═════════════════════════════════════════════╣";									os.system('echo ' + string)
		string = "║                ADVERTENCIA                  ║";									os.system('echo ' + string)
		string = "║         ────────────────────────            ║"; 								os.system('echo ' + string)
		string = "║                                             ║";									os.system('echo ' + string)
		string = "║      FALTA UN ARGUMENTO EN LA CADENA...     ║";									os.system('echo ' + string)
		string = "║                                             ║";									os.system('echo ' + string)
		string = "║ Verifique que ha ingresado los 2 argumentos ║";									os.system('echo ' + string)
		string = "║     necesarios para ejecutar el script.     ║";									os.system('echo ' + string)
		string = "║                                             ║";									os.system('echo ' + string)
		string = "║ Ej: python crear nombre_proyecto nombre_app ║";									os.system('echo ' + string)
		string = "╚═════════════════════════════════════════════╝";									os.system('echo ' + string)
		sys.exit()
	project = sys.argv[1]
	app = sys.argv[2]
	if not os.path.exists(project):
		# print(f'╣ ║ ╗ ╝ ╚ ╔ ╩ ╦ ╠ ═ ╬ ')
		if os.system(f'django-admin startproject {project}') == 0:
			os.system('clear')		
			string = '.';																			os.system('echo ' + string)
			string = '..';																			os.system('echo ' + string)
			string = '...';																			os.system('echo ' + string)
			string = "╔═════════════════════════════════════════════╗";								os.system('echo ' + string)
			string = "║     GENERADOR DE PROYECTOS DJANGO  v" + version + "     ║";					os.system('echo ' + string)
			string = "╚═════════════════════════════════════════════╝";								os.system('echo ' + string)
			string = '...';																			os.system('echo ' + string)
			string = '..';																			os.system('echo ' + string) 
			string = '.';																			os.system('echo ' + string)
			string = '... GENERANDO PROYECTO: "' + project + '"'
			os.system('echo ' + string)
		else:
			os.system('clear')
			string = "╔═════════════════════════════════════════════╗"; 							os.system('echo ' + string)
			string = "║     GENERADOR DE PROYECTOS DJANGO  v" + version + "     ║";					os.system('echo ' + string)
			string = "╠═════════════════════════════════════════════╣";								os.system('echo ' + string)
			string = "║                ADVERTENCIA                  ║";								os.system('echo ' + string)
			string = "║         ────────────────────────            ║"; 							os.system('echo ' + string)
			string = "║                                             ║";								os.system('echo ' + string)
			string = "║    COMANDO django-admin no encontrado...    ║";								os.system('echo ' + string)
			string = "║                                             ║";								os.system('echo ' + string)
			string = "║    Verifique antes de continuar que en su   ║";								os.system('echo ' + string)
			string = "║   consola se encuentre en un ambiente con   ║";								os.system('echo ' + string)
			string = "║              django habilitado.             ║";								os.system('echo ' + string)
			string = "╚═════════════════════════════════════════════╝";								os.system('echo ' + string)
			quit()
	else:
		os.system('clear')
		string = "╔═════════════════════════════════════════════╗"; 								os.system('echo ' + string)
		string = "║     GENERADOR DE PROYECTOS DJANGO  v" + version + "     ║";						os.system('echo ' + string)
		string = "╠═════════════════════════════════════════════╣";									os.system('echo ' + string)
		string = "║                ADVERTENCIA                  ║";									os.system('echo ' + string)
		string = "║         ────────────────────────            ║"; 								os.system('echo ' + string)
		string = "║                                             ║";									os.system('echo ' + string)
		string = "║        NOMBRE DE PROYECTO EXISTE...         ║";									os.system('echo ' + string)
		string = "║                                             ║";									os.system('echo ' + string)
		string = "║ Verifique que la carpeta con el nombre del  ║";									os.system('echo ' + string)
		string = "║ proyecto a crear, NO exista en la carpeta.  ║";									os.system('echo ' + string)
		string = "╚═════════════════════════════════════════════╝";									os.system('echo ' + string)
		quit()
	create_app(project, app)


if __name__ == '__main__':
    main()
