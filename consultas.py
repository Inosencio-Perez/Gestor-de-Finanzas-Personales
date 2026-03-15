from db_config import obtener_conexion

def registrar_transaccion(fecha, descripcion, categoria, tipo, monto):
    """Inserta un nuevo movimiento en la base de datos."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        sql = """INSERT INTO transacciones (fecha, descripcion, categoria, tipo, monto) 
                 VALUES (%s, %s, %s, %s, %s)"""
        valores = (fecha, descripcion, categoria, tipo, monto)
        
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"\n✅ Registro exitoso: {descripcion} ({categoria})")
    except Exception as e:
        print(f"❌ Error al registrar en la base de datos: {e}")
    finally:
        cursor.close()
        conexion.close()

def listar_transacciones():
    """Muestra todos los movimientos en un formato de tabla limpia."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, fecha, descripcion, categoria, tipo, monto FROM transacciones ORDER BY fecha DESC")
        registros = cursor.fetchall()

        if not registros:
            print("\n📭 No hay movimientos registrados aún.")
            return

        print("\n" + "="*85)
        print(f"{'ID':<4} | {'FECHA':<12} | {'DESCRIPCIÓN':<18} | {'CATEGORÍA':<12} | {'TIPO':<8} | {'MONTO':>10}")
        print("-" * 85)
        
        for reg in registros:
            # Desempaquetamos los 6 campos
            id_t, fecha, desc, cat, tipo, monto = reg
            print(f"{id_t:<4} | {str(fecha):<12} | {desc:<18} | {cat:<12} | {tipo:<8} | ${monto:>9.2f}")
        print("="*85)

    except Exception as e:
        print(f"❌ Error al listar: {e}")
    finally:
        cursor.close()
        conexion.close()

def obtener_saldo_total():
    """Calcula el balance total restando egresos de ingresos."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        
        # Sumamos ingresos
        cursor.execute("SELECT SUM(monto) FROM transacciones WHERE tipo = 'Ingreso'")
        ingresos = cursor.fetchone()[0] or 0.0
        
        # Sumamos egresos
        cursor.execute("SELECT SUM(monto) FROM transacciones WHERE tipo = 'Egreso'")
        egresos = cursor.fetchone()[0] or 0.0
        
        saldo = ingresos - egresos
        
        print("\n" + "📊 " + " RESUMEN DE CUENTA ".center(30, "—"))
        print(f"  (+) Ingresos Totales:  ${ingresos:>10.2f}")
        print(f"  (-) Egresos Totales:   ${egresos:>10.2f}")
        print("-" * 34)
        print(f"  (=) SALDO ACTUAL:      ${saldo:>10.2f}")
        print("—" * 34)

    except Exception as e:
        print(f"❌ Error al calcular saldo: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_transaccion(id_transaccion):
    """Elimina un registro específico por su ID."""
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM transacciones WHERE id = %s"
        cursor.execute(sql, (id_transaccion,))
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f"\n🗑️  Registro #{id_transaccion} eliminado correctamente.")
        else:
            print(f"\n⚠️ No se encontró ningún registro con el ID {id_transaccion}.")
            
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
    finally:
        cursor.close()
        conexion.close()