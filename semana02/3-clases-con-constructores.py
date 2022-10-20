class Documento:
    def __init__(self, tipo, num_paginas, editable, contenido):
        self.tipo = tipo
        self.num_paginas = num_paginas
        self.editable = editable
        self.contenido = contenido
    def editar_documento(self, nuevo_contenido):
        if self.editable == False:
            print("Este documento no puede ser modificado")
        else:
            self.contenido = nuevo_contenido
            print("El archivo fue madifcado")
        
mi_curriculum = Documento("pdf", 10, False, "Soy developoer")

proforma_pagina_web = Documento ("word", 200, True, "son 2500 soles")

mi_curriculum.editar_documento("Soy desarrollador de python")
proforma_pagina_web.editar_documento("son 3000 soles")

#abstraccion es 