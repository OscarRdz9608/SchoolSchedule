-- Database: horarios

DROP TABLE IF EXISTS usuarios;

-- Administrador, secretaría academica, coordinador academico, coordinador idiomas, docente
CREATE TYPE user_type AS ENUM ('1', '2', '3', '4', '5');

CREATE TABLE IF NOT EXISTS usuarios (
  id_usuario SERIAL PRIMARY KEY,
  nombre_usuario VARCHAR(20),
  apellido_paterno VARCHAR(15),
  apellido_materno VARCHAR(15),
  email VARCHAR(60) UNIQUE,
  tipo_usuario user_type
);

SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';
  
CREATE TYPE periodos AS ENUM ('1', '2', '3');

DROP TABLE IF EXISTS ciclo_escolar;
CREATE TABLE IF NOT EXISTS ciclo_escolar(
  id_ciclo_escolar SERIAL PRIMARY KEY,
  periodo periodos,
  anio SMALLINT,
    registro_grupos_inicio DATE,
    registro_grupos_termino DATE,
    registro_disponibilidad_inicio DATE,
    registro_disponibilidad_termino DATE,
    registro_contrataciones_inicio DATE,
    registro_contrataciones_termino DATE,
    registro_horarios_secretaria_inicio DATE,
    registro_horarios_secretaria_termino DATE,
    registro_aprobacion_coordi_docente_inicio DATE,
    registro_aprobacion_coordi_docente_termino DATE
);

DROP TABLE IF EXISTS carreras;
CREATE TABLE IF NOT EXISTS carreras(
  id_carrera SERIAL PRIMARY KEY,
  nombre_carrera VARCHAR(60),
  coordinador_carrera INTEGER REFERENCES usuarios(id_usuario)
);

DROP TABLE IF EXISTS plan_estudios;
CREATE TABLE IF NOT EXISTS plan_estudios(
  id_materia SERIAL PRIMARY KEY,
  nombre_materia VARCHAR(60),
  cuatrimestre SMALLINT,
  total_horas SMALLINT,
  total_horas_semana SMALLINT,
  carrera SMALLINT REFERENCES carreras(id_carrera)
);


DROP TABLE IF EXISTS turnos;
CREATE TABLE IF NOT EXISTS turnos(
  id_turno SERIAL PRIMARY KEY,
  nombre_turno VARCHAR(15),
  hora_entrada TIME,
  hora_salida TIME
);.