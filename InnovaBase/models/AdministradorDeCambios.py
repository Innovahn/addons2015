from openerp.osv import fields, osv
import os
import shutil
import time

class administradorcambios(osv.Model):
    _name = 'innovabase.administradorcambios'
	_columns = {
    'path': fields.text('path'),
	'active': fields.boolean('activo'),
    }

	def create(self, cr, uid, vals, context=None):
		config_id = super(administradorcambios, self).create(cr, uid, vals, context=context)

		RutaArchivos = vals['path']
		infile = open(RutaArchivos+'/configuracion.txt', 'r')

        # recorremos el archivo linea por linea
        for line in infile:
        	# ignora cualquier linea que no empiece por el simbolo >
        	if line.startswith('>'):
	    		# rutas[1] es el archivo alojado dentro de la carpeta archivos que se desea copiar
        		# rutas[2] es la ruta donde deseamos copiar el archivo
                rutas = line.split('>')
                #si se va a sustituir un archivo sacamos un respaldo del archivo
	            if os.path.exists(os.getcwd()+'/'+rutas[2].lstrip()[:-1]):
					os.rename(os.getcwd()+'/'+rutas[2].lstrip()[:-1],os.getcwd()+'/'+rutas[2].lstrip()[:-1]+time.strftime('%d %b %Y'))
        	    #copia el archivo rutas[1] en la ubicacion rutas[2]
				shutil.copyfile(RutaArchivos+'/'+rutas[1].lstrip()[:-1],os.getcwd()+'/'+rutas[2].lstrip()[:-1])
