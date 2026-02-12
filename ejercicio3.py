
config_base = {"host": "localhost", "port": 3306, "debug": False}
config_desarrollo = {"debug": True, "log_level": "verbose"}
config_produccion = {"host": "192.168.1.10", "log_level": "error"}

config_final_dev = {**config_base, **config_desarrollo}
config_final_prod = {**config_base, **config_produccion}

def conectar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

print("--- Configuración Desarrollo ---")
conectar(**config_final_dev)

print("\n--- Configuración Producción ---")
conectar(**config_final_prod)

