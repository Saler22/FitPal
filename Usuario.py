class Usuario:
    def __init__(self, id_usuario, nombre, edad, genero, altura, peso):
        """
        Constructor de la clase Usuario.
        
        Parámetros:
        id_usuario (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        edad (int): Edad del usuario.
        genero (str): Género del usuario.
        altura (float): Altura del usuario en metros.
        peso (float): Peso del usuario en kilogramos.
        """
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.altura = altura
        self.peso = peso
    

    def crear_usuario(self):
        """
        Método de clase para crear un nuevo usuario.
        
        Retorna:
        Usuario: Instancia de la clase Usuario con los datos ingresados por el usuario.
        """

    def editar_usuario(self):
        """
        Método para editar los datos de un usuario existente.
        """

