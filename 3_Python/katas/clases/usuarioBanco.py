class UsuarioBanco:
    """
    Representa a un usuario de banco con nombre, saldo y si tiene cuenta corriente.

    Atributos:
        nombre (str): Nombre del titular.
        saldo (float): Saldo actual del usuario.
        cuenta_corriente (bool): Si dispone de cuenta corriente para operar.
    """
    def __init__(self, nombre, saldo, cuenta_corriente):
        """
        Inicializa el usuario.

        Args:
            nombre: Nombre del usuario (no vacío).
            saldo: Saldo inicial (numérico).
            cuenta_corriente: True si tiene cuenta corriente, False en caso contrario.
        """
        
        # Algunas comprobaciones
        if not isinstance(nombre, str) or not nombre.strip():
            raise TypeError("nombre debe ser str no vacío")
        if not isinstance(saldo, (int, float)) or isinstance(saldo, bool):
            raise TypeError("saldo debe ser numérico")
        if saldo < 0:
            raise ValueError("saldo no puede ser negativo")
        if not isinstance(cuenta_corriente, bool):
            raise TypeError("cuenta_corriente debe ser bool")
        
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente
        
    def retirar_dinero(self, cantidad):
        """Resta del saldo si hay fondos."""
        try:
            self.saldo -= cantidad
        except:
            return "No se puede retirar dinero de la cuenta"
        
    def transferir_dinero(self, cliente_transfiere, cantidad):
        """
        Transfiere desde `cliente_transfiere` hacia `self`.
        """
        if not isinstance(cliente_transfiere, UsuarioBanco):
            raise TypeError("destino debe ser Cuenta")
        elif cantidad <= 0:
            raise ValueError("cantidad debe ser > 0")
        elif cliente_transfiere.saldo < cantidad:
            print(f"Debes tener al menos {cantidad} para poder hacer la transferencia")
        else:
            cliente_transfiere.saldo -= cantidad
            self.saldo += cantidad
        

    def agregar_dinero(self, cantidad):
        """Suma al saldo."""
        try:
            self.saldo += cantidad
        except:
            return "No se puede agregar dinero a la cuenta"