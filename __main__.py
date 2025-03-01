from src.modelo.cancion import Cancion
from src.modelo.interprete import Interprete
from src.modelo.album import Album, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
   #Crea la BD
   #Base.metadata.create_all(engine)

   #Abre la sesion
   session = Session()

   '''#delete
   cancion = session.query(Cancion).get(2)
   session.delete(cancion)
   session.commit()
   session.close()
   '''
   
   '''#update
   cancion = session.query(Cancion).get(2)
   interprete = session.query(Interprete).get(4)

   cancion.minutos = 5
   cancion.segundos = 30
   cancion.compositor = "Pedro Pérez"
   cancion.interpretes.append(interprete)
   session.add(cancion)
   session.commit()
   session.close()   
   '''
   
   '''#consulta
   canciones = session.query(Cancion).filter(Cancion.interpretes.contains(session.query(Interprete).filter(Interprete.nombre == "Aldo Gavilan").first())).all()

   for cancion in canciones:
      print("Titulo: " + cancion.titulo + " (00:" +
            str(cancion.minutos) + ":" +
            str(cancion.segundos) + ")")

      print("Intérpretes")
      for interprete in cancion.interpretes:
          print(" - " + interprete.nombre)

      for album in cancion.albumes:
          print(" -- Presente en el album: " + album.titulo)

      print("")

   
   session.close()
   '''

   '''#crear interpretes
   interprete1 = Interprete(nombre = "Samuel Torres", texto_curiosidades = "Es colombiano y vive en NY")
   interprete2 = Interprete(nombre = "Aldo Gavilan", texto_curiosidades = "Canto a Cuba")
   interprete3 = Interprete(nombre = "Buena Vista Social club")
   interprete4 = Interprete(nombre = "Arturo Sandoval", texto_curiosidades = "No sabia quien era")
   session.add(interprete1)
   session.add(interprete2)
   session.add(interprete3)
   session.add(interprete4)
   session.commit()

   # Crear albumes
   album1 = Album(titulo = "Latin Jazz Compilation", ano = 2021, descripcion = "Album original", medio = Medio.DISCO)
   album2 = Album(titulo = "Bandas sonoras famosas", ano = 2021, descripcion = "Compilacion", medio = Medio.DISCO)
   session.add(album1)
   session.add(album2)


   # Crear canciones
   cancion1 = Cancion(titulo = "Ajiaco", minutos = 3, segundos = 1, compositor = "Samuel Torres")
   cancion2 = Cancion(titulo = "Forced Displacement", minutos = 3, segundos = 12, compositor = "Desconocido")
   cancion3 = Cancion(titulo = "Alegria", minutos = 4, segundos = 27, compositor = "AU")
   session.add(cancion1)
   session.add(cancion2)
   session.add(cancion3)

   # Relacionar albumes con canciones
   album1.canciones = [cancion1, cancion2]
   album2.canciones = [cancion1, cancion3]

   # Relacionar canciones con interpretes
   cancion1.interpretes = [interprete1]
   cancion2.interpretes = [interprete2]
   cancion3.interpretes = [interprete3, interprete4]
   session.commit()

   session.commit()
   session.close()'''