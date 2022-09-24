from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, VARCHAR
from config.db import meta, engine

usuarios = Table("usuarios", meta,
              Column("id_usuario", Integer, primary_key=True),
              Column("nombre_usuario", VARCHAR(20)),
              Column("passw", VARCHAR(255)),
              Column("jugador", Integer),
              Column("nivel", Integer))
meta.create_all(engine)