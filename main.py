from consultas import (
    registrar_transaccion, 
    listar_transacciones, 
    obtener_saldo_total, 
    eliminar_transaccion
)
from datetime import date

def menu():
    while True:
        print("\n" + "═"*45)
        print("      GESTOR DE FINANZAS PERSONAL v2.5 💰")
        print("═"*45)
        print(" 1. ➕ Registrar Ingreso o Egreso")
        print(" 2. 📜 Ver Historial de Movimientos")
        print(" 3. 📊 Ver Saldo Actual (Balance)")
        print(" 4. 🗑️  Eliminar un Movimiento (por ID)")
        print(" 5. 🚪 Salir")
        print("═"*45)
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            print("\n--- NUEVO REGISTRO ---")
            f_input = input("Fecha (AAAA-MM-DD) [Enter para hoy]: ")
            fecha = f_input if f_input else date.today()
            
            desc = input("Descripción (ej. Supermercado, Sueldo): ")
            
            # --- NUEVA CATEGORÍA ---
            print("Categorías sugeridas: Comida, Renta, Transporte, Ocio, Salud, etc.")
            cat = input("Categoría: ").capitalize()
            if not cat: cat = "General" # Valor por defecto si se deja vacío
            
            tipo = input("Tipo (Ingreso/Egreso): ").capitalize()
            
            if tipo not in ["Ingreso", "Egreso"]:
                print("⚠️ Error: El tipo debe ser 'Ingreso' o 'Egreso'.")
                continue

            try:
                monto = float(input("Monto (ej. 1500.50): "))
                # Enviamos los 5 datos a la función de consultas
                registrar_transaccion(fecha, desc, cat, tipo, monto)
            except ValueError:
                print("❌ Error: El monto debe ser un número válido.")
            
        elif opcion == "2":
            listar_transacciones()
            
        elif opcion == "3":
            obtener_saldo_total()
            
        elif opcion == "4":
            listar_transacciones()
            try:
                id_a_borrar = int(input("\nEscriba el ID del registro que desea eliminar: "))
                confirmar = input(f"⚠️ ¿Seguro que desea eliminar el registro #{id_a_borrar}? (s/n): ").lower()
                
                if confirmar == 's':
                    eliminar_transaccion(id_a_borrar)
                else:
                    print("Operación cancelada.")
            except ValueError:
                print("❌ Error: Debe ingresar un número de ID válido.")
            
        elif opcion == "5":
            print("\n💾 Desconectando..." \
            "")
            break
        else:
            print("\n⚠️ Opción no válida.")

if __name__ == "__main__":
    menu()