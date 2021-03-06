from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os


app = Flask(__name__)


#IMPLEMENTAR CORS PARA NO TENER ERRORES AL TRATAR ACCEDER AL SERVIDOR DESDE OTRO SERVER EN DIFERENTE LOCACIÓN
CORS(app)

DB_HOST = "localhost"
DB_NAME = "proyecto1"
DB_USER = "jd1_jose"
DB_PASS = "1234"
try:
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST)
    
    cur = con.cursor()
    

    print(con.status)
    

    @app.route("/")
    def hello():
      return """<h1 style='color:blue'>Practica1 !</h1>
                """

#obtengo todos los registros de mi tabla movies que cree en mi BD
    @app.route('/consulta1', methods=['get'])
    def cl1():
        consulta1='select  a.id_pelicula,b.id_tienda from pelicula as a, pelicula_tienda as b where a.nombre_pelicula="SUGAR WONKA" and a.id_pelicula= b.id_pelicula'
        cur.execute('select  a.id_pelicula,b.id_tienda from pelicula as a, pelicula_tienda as b where a.nombre_pelicula=''\'SUGAR WONKA''\' and a.id_pelicula= b.id_pelicula')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta2', methods=['get'])
    def cl2():
        consulta2='select (b.nombre|' '|b.apellido) as name1, sum(monto_pagar)as total_a_pagar from renta as a, cliente as b group  by a.id_cliente,name1,b.id_cliente having count(a.id_cliente)>=40 and a.id_cliente=b.id_cliente'
        cur.execute(consulta2)
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta3', methods=['get'])
    def cl3():
        consulta3='select * from actores where  nombre_actores like ''\'%son%''\''
        cur.execute(consulta3)
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta4', methods=['get'])
    def cl4():
        cur.execute('select distinct c.nombre_actores,b.pelicula_año from pelicula_actor as a, pelicula as b, actores as c group by a.id_pelicula,c.nombre_actores,b.pelicula_año, b.descripcion, b.id_pelicula having b.descripcion like ''\'%Shark%''\' and b.descripcion like ''\'%Crocodile%''\' and  a.id_pelicula=b.id_pelicula')
        rows = cur.fetchall()
        

        return jsonify(rows)
    @app.route('/consulta5', methods=['get'])
    def cl5():
        cur.execute('select (Select pa.nombre_pais from pais as pa where pa.id_pais= b.pais),(b.nombre|' '|b.apellido) as name1, (((select distinct max(count (id_cliente)) OVER () as maxima_renta from renta group by id_cliente)/(select distinct count (renta.id_cliente) from renta as renta inner join cliente cl on cl.id_cliente= renta.id_renta inner join ciudad ci on ci.id_ciudad=cl.id_cliente inner join pais pa on pa.id_pais=cl.pais group by renta.id_cliente, cl.id_cliente, pa.id_pais))) from renta as a, cliente as b group  by a.id_cliente,name1,b.id_cliente having count(a.id_cliente)=(select distinct max(count (id_cliente)) OVER () as maxima_renta from renta group by id_cliente) and a.id_cliente=b.id_cliente')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta6', methods=['get'])
    def cl6():
        cur.execute('select * from pelicula')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta7', methods=['get'])
    def cl7():
        cur.execute("select * from pelicula")
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta8', methods=['get'])
    def cl8():
        cur.execute("select * from pelicula")
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta9', methods=['get'])
    def cl9():
        cur.execute("select * from pelicula")
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/consulta10', methods=['get'])
    def cl10():
        cur.execute("select * from pelicula")
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/eliminarTemporal', methods=['get'])
    def eliminarTemporal():
        cur.execute('Drop table temporal;')
        con.commit()
        return "Tabla temporal Eliminada"

    @app.route('/eliminarModelo', methods=['get'])
    def eliminarModelo():
        cur.execute("""
        Drop table pelicula_actor CASCADE;
        Drop table pelicula_tienda CASCADE;
        Drop table renta_pelicula CASCADE;
        Drop table renta_cliente CASCADE;
        Drop table pelicula CASCADE;
        Drop table categoria_pelicula CASCADE;
        Drop table actores CASCADE;
        Drop table renta CASCADE;
        Drop table tienda CASCADE;
        Drop table cliente CASCADE;
        Drop table empleado CASCADE;
        Drop table ciudad CASCADE;
        Drop table clasificacion_pelicula CASCADE;
        Drop table estado CASCADE;
        Drop table pais CASCADE;
        """)
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    @app.route('/cargarTemporal', methods=['get'])
    def cargaTemporal():
        cur.execute("""
        create table public.temporal(
        NOMBRE_CLIENTE varchar(45),
        CORREO_CLIENTE varchar(45),
        CLIENTE_ACTIVO varchar(10),
        FECHA_CREACION varchar(50),
        TIENDA_PREFERIDA varchar(45),
        DIRECCION_CLIENTE varchar(50),
        CODIGO_POSTAL_CLIENTE varchar(50),
        CIUDAD_CLIENTE varchar(50),
        PAIS_CLIENTE varchar(50),
        FECHA_RENTA varchar(50),
        FECHA_RETORNO varchar(50),
        MONTO_A_PAGAR varchar(50),
        FECHA_PAGO varchar(50),
        NOMBRE_EMPLEADO varchar(50),
        CORREO_EMPLEADO	varchar (50),
        EMPLEADO_ACTIVO	varchar(10),
        TIENDA_EMPLEADO varchar(20),
        USUARIO_EMPLEADO varchar(10),
        CONTRASEÑA_EMPLEADO varchar(250),
        DIRECCION_EMPLEADO varchar (100),
        CODIGO_POSTAL_EMPLEADO varchar(10),
        CIUDAD_EMPLEADO varchar(100),
        PAIS_EMPLEADO varchar(100),
        NOMBRE_TIENDA varchar(100),
        ENCARGADO_TIENDA varchar(50),
        DIRECCION_TIENDA varchar(45),
        CODIGO_POSTAL_TIENDA varchar(10),
        CIUDAD_TIENDA varchar(50),
        PAIS_TIENDA varchar(50),
        TIENDA_PELICULA varchar(50),
        NOMBRE_PELICULA	varchar (50),
        DESCRIPCION_PELICULA varchar(500),
        ANIO_LANZAMIENTO varchar(50),
        DIAS_RENTA varchar(50),
        COSTO_RENTA	varchar(50),
        DURACION varchar(50),
        COSTO_POR_DAÑO varchar(50),
        CLASIFICACION varchar(10),
        LENGUAJE_PELICULA varchar(45),
        CATEGORIA_PELICULA varchar(50),
        ACTOR_PELICULA varchar(50)
        );
        COPY public.temporal From ''\'/home/jose/Escritorio/Practica1/BlockbusterData.csv''\' DELIMITER ''\';''\' CSV HEADER
        """)
        con.commit()
        return "Carga de Datos exitosa"
    @app.route('/cargarModelo', methods=['get'])
    def cargaModelo():
        cur.execute("""

            create table estado(
            id_Estado int GENERATED ALWAYS AS IDENTITY primary key,
            nombreEstado varchar(45)
            );
            create table ciudad(
            id_Ciudad int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_Ciudad varchar(100)
            );
            create table pais(
            id_Pais int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_Pais varchar(100)
            );
            Create table cliente(
            id_Cliente int GENERATED ALWAYS AS IDENTITY primary key,
            nombre varchar(45),
            apellido varchar(45),
            correo varchar (100),
            direccion varchar(100),
            fecha_Creacion date,
            tienda_Fav    varchar(45),
            codigo_postal int,
            estado int,
            ciudad int,
            pais int,
            CONSTRAINT fk_estado
                FOREIGN KEY(estado) 
                REFERENCES estado(id_estado),
            CONSTRAINT fk_ciudad
                FOREIGN KEY(ciudad) 
                REFERENCES ciudad(id_ciudad),
            CONSTRAINT fk_pais
                FOREIGN KEY(pais) 
                REFERENCES pais(id_pais)
            );
            create table categoria_pelicula(
            id_categoria int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_categoria varchar(100)
            );
            create table clasificacion_pelicula(
            id_clasificacion int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_clasificacion varchar(100)
            );
            create table actores(
            id_actores int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_actores varchar(100)
            );
            create table tienda(
            id_tienda int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_tienda varchar(100),
            encargado_tienda varchar(100),
            direccion_tienda varchar(100),
            codigo_postal_tienda int,
            ciudad int,
            pais int,
            CONSTRAINT fk_ciudad
                FOREIGN KEY(ciudad) 
                REFERENCES ciudad(id_ciudad),
            CONSTRAINT fk_pais
                FOREIGN KEY(pais) 
                REFERENCES pais(id_pais)
            );
            create table pelicula(
            id_pelicula int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_pelicula varchar(50),
            descripcion varchar(150),
            pelicula_año int,
            duracion int,
            idioma_pelicula varchar(50),
            dias_renta int,
            costo_renta float,
            costo_daño float,
            id_categoria int,
            id_clasificacion int,
            CONSTRAINT fk_categoria
                FOREIGN KEY(id_categoria) 
                REFERENCES categoria_pelicula(id_categoria),
            CONSTRAINT fk_clasificacion
                FOREIGN KEY(id_clasificacion) 
                REFERENCES clasificacion_pelicula(id_clasificacion)
            );
            create table empleado(
            id_empleado int GENERATED ALWAYS AS IDENTITY primary key,
            nombre_empleado varchar(45),
            apellido_empleado varchar(45),
            usuario_empleado varchar(50),
            contraseña_empleado varchar(250),
            direccion_empleado varchar(75),
            correo_empleado varchar(75),
            codigo_postal int,
            ciudad int,
            pais int,
            tienda int,
            estado int,
            CONSTRAINT fk_ciudad
                FOREIGN KEY(ciudad) 
                REFERENCES ciudad(id_ciudad),
            CONSTRAINT fk_pais
                FOREIGN KEY(pais) 
                REFERENCES pais(id_pais),
            CONSTRAINT fk_tienda
                FOREIGN KEY(tienda) 
                REFERENCES tienda(id_tienda),
            CONSTRAINT fk_estado
                FOREIGN KEY(estado) 
                REFERENCES estado(id_estado)
            );
            create table pelicula_actor(
            id_pelicula int references pelicula(id_pelicula),
            id_actor int references actores(id_actores),
            CONSTRAINT pelicula_actor_pkey PRIMARY KEY (id_pelicula, id_actor)  
            );
            create table pelicula_tienda(
            id_pelicula int references pelicula(id_pelicula),
            id_tienda int references tienda(id_tienda),
            CONSTRAINT pelicula_tienda_pkey PRIMARY KEY (id_pelicula, id_tienda)  
            );
            create table renta(
            id_renta int GENERATED ALWAYS AS IDENTITY primary key,
            fecha_renta date,
            fecha_retorno date,
            monto_pagar float,
            fecha_pago date,
            id_empleado int,
            id_cliente int,
            CONSTRAINT fk_renta_empleado
            FOREIGN KEY(id_empleado) 
                REFERENCES empleado(id_empleado),
            CONSTRAINT fk_renta_cliente
            FOREIGN KEY(id_cliente) 
                REFERENCES cliente(id_cliente)
            );
            create table renta_pelicula(
            id_pelicula int references pelicula(id_pelicula),
            id_renta int references renta(id_renta),
            CONSTRAINT pelicula_renta_pkey PRIMARY KEY (id_pelicula, id_renta)  
            );

            insert into ciudad (nombre_ciudad) 
            select distinct ciudad_cliente
            from temporal
            where ciudad_cliente !='-' 
            union 
            select distinct ciudad_empleado
            from temporal
            where ciudad_empleado !='-' 
            union 
            select distinct ciudad_tienda
            from temporal
            where ciudad_tienda !='-' 
            order by 
            ciudad_cliente asc;
            -----------------------------------------------
            insert into pais (nombre_pais) 
            select distinct pais_cliente
            from temporal
            where pais_cliente !='-' 
            union 
            select distinct pais_empleado
            from temporal
            where pais_empleado !='-' 
            union 
            select distinct pais_tienda
            from temporal
            where pais_tienda !='-' 
            order by 
            pais_cliente asc;
            -----------------------------------------------
            insert into estado (nombreestado) 
            select distinct cliente_activo
            from temporal
            where cliente_activo !='-' 
            union 
            select distinct empleado_activo
            from temporal
            where empleado_activo !='-' ;
            -----------------------------------------------
            insert into categoria_pelicula(nombre_categoria)
            select distinct CATEGORIA_PELICULA
            from temporal
            where CATEGORIA_PELICULA !='-' 
            order by 
            CATEGORIA_PELICULA asc;
            ------------------------------------------------
            insert into clasificacion_pelicula(nombre_clasificacion)
            select distinct clasificacion
            from temporal
            where clasificacion !='-'
            order by
            clasificacion asc;
            ------------------------------------------------------------
            insert into pelicula(id_clasificacion, id_categoria, costo_daño,costo_renta, dias_renta, pelicula_año,duracion,nombre_pelicula, descripcion, idioma_pelicula)
            select distinct b.id_clasificacion,c.id_categoria, cast(costo_por_daÑo as float),cast(costo_renta as float),cast(dias_renta as integer), cast(anio_lanzamiento as integer),cast( duracion as integer),nombre_pelicula, descripcion_pelicula, lenguaje_pelicula
            from temporal as a , categoria_pelicula as c, clasificacion_pelicula as b
            where nombre_pelicula !='-' and c.nombre_categoria =a.categoria_pelicula and b.nombre_clasificacion =a.clasificacion
            order by nombre_pelicula asc;
            -----------------------------------------------------------------------------------------------------
            insert into tienda (nombre_tienda,encargado_tienda, direccion_tienda, ciudad, pais)
            select distinct   nombre_tienda,encargado_tienda,direccion_tienda, a.id_ciudad, b.id_pais
            from temporal as c, ciudad as a, pais as b
            where nombre_tienda!='-' and c.pais_tienda=b.nombre_pais and c.ciudad_tienda =a.nombre_ciudad
            order by nombre_tienda asc;
            --------------------------------------------------------------------------------------------------
            insert into cliente (direccion,nombre, apellido, correo, fecha_creacion, tienda_fav, codigo_postal, estado, ciudad, pais)
            Select distinct 
            direccion_cliente,
            split_part(nombre_cliente::TEXT, ' ', 1)nombre,
            split_part(nombre_cliente::TEXT, ' ', 2)Apellido,
            correo_cliente,
            TO_DATE(fecha_creacion::TEXT,'DD M YYY'),
            tienda_preferida,
            to_number(codigo_postal_cliente,'99G999D9S'),
            d.id_estado,
            b.id_ciudad,
            c.id_pais
            from temporal as a, ciudad as b, pais as c, estado as d
            where a.nombre_cliente != '-' and a.ciudad_cliente=b.nombre_ciudad and a.pais_cliente=c.nombre_pais and a.cliente_activo=d.nombreestado
            order by correo_cliente asc;
            ------------------------------------------------------------------------------------------
            insert into empleado (nombre_empleado, apellido_empleado,correo_empleado, usuario_empleado, contraseña_empleado,direccion_empleado, estado, ciudad, pais,tienda)
            Select distinct 
            split_part(nombre_empleado::TEXT, ' ', 1)nombre,
            split_part(nombre_empleado::TEXT, ' ', 2)Apellido,
            correo_empleado,
            usuario_empleado,
            contraseÑa_empleado,
            direccion_empleado,
            d.id_estado,
            b.id_ciudad,
            c.id_pais,
            e.id_tienda
            from temporal as a, ciudad as b, pais as c, estado as d, tienda as e
            where a.nombre_empleado != '-' and a.ciudad_empleado=b.nombre_ciudad and a.pais_empleado=c.nombre_pais and a.empleado_activo=d.nombreestado and a.tienda_empleado= e.nombre_tienda
            order by correo_empleado asc;
            ------------------------------------------------------------------
            insert into actores(nombre_actores)
            select distinct actor_pelicula from temporal
            where actor_pelicula!='-'
            order by actor_pelicula;
            -------------------------------------------------------------------------------
            insert into  pelicula_actor(id_pelicula, id_actor) 
            select distinct b.id_pelicula, c.id_actores
            from temporal as a, pelicula as b, actores as c
            where a.nombre_pelicula =b.nombre_pelicula and a.actor_pelicula = c.nombre_actores
            order by b.id_pelicula asc;
            ----------------------------------------------------------------------
            insert into pelicula_tienda(id_pelicula, id_tienda)
            select distinct c.id_pelicula,b.id_tienda
            from temporal as a, tienda as b, pelicula as c
            where a.nombre_pelicula!='-' and a.nombre_pelicula =c.nombre_pelicula and a.tienda_pelicula= b.nombre_tienda 
            order by c.id_pelicula asc;
            --------------------------------------------------------------------------
            insert into renta(id_cliente, fecha_renta, fecha_retorno, monto_pagar, fecha_pago, id_empleado)
            select distinct  b.id_cliente,
            TO_DATE(fecha_renta::TEXT,'DD M YYY'),
            TO_DATE(fecha_retorno::TEXT,'DD M YYY'),
            CAST(monto_a_pagar as float), 
            TO_DATE(fecha_pago::TEXT,'DD M YYY'),
            c.id_empleado
            from temporal as a, cliente as b, empleado as c
            where a.nombre_cliente!='-' and fecha_retorno!='-' and fecha_renta!='-' and fecha_pago!='-'and monto_a_pagar!='-'
            and a.correo_cliente=b.correo and a.correo_empleado=c.correo_empleado;
            ----------------------------------------------------------------------------
            insert into renta_pelicula(id_renta, id_pelicula)
            select distinct  d.id_renta,c.id_pelicula 
            from temporal as a,cliente as b, pelicula as c, renta as d
            where a.fecha_renta!='-' and a.nombre_pelicula!='-' and a.nombre_cliente!='-'
            and a.correo_cliente=b.correo
            and a.nombre_pelicula=c.nombre_pelicula
            and b.id_cliente=d.id_cliente; 
        
        """)
        con.commit()
        return "Carga de modelo de datos exitosa"
   
        
    if __name__ == "__main__":
     app.run(host='0.0.0.0')        

except:
    print('Error')