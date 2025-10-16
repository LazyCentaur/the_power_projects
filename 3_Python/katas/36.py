# PROYECTO LÓGICA: Katas de Python: Ejercicio 36

# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
# agregar dinero al saldo.
# Código a seguir:
# 1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante True y False.
# 2. Implementar el método retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no poder hacerse.
# 3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual.
# Lanzará un error en caso de no poder hacerse.
# 4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
# Caso de uso:
# 1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
# 2. Agregar 20 unidades de saldo de "Bob".
# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
# 4. Retirar 50 unidades de saldo a "Alicia".

from clases.usuarioBanco import UsuarioBanco

usuarioAlicia = UsuarioBanco("Alicia", 100, True)
usuarioBob = UsuarioBanco("Bob", 50, True)

print(f"Alicia: {usuarioAlicia.saldo}")
print(f"Bob: {usuarioBob.saldo}")

usuarioBob.agregar_dinero(20)

print(f"Alicia: {usuarioAlicia.saldo}")
print(f"Bob: {usuarioBob.saldo}")

usuarioAlicia.transferir_dinero(usuarioBob, 80)

print(f"Alicia: {usuarioAlicia.saldo}")
print(f"Bob: {usuarioBob.saldo}")

usuarioAlicia.retirar_dinero(50)

print(f"Alicia: {usuarioAlicia.saldo}")
print(f"Bob: {usuarioBob.saldo}")