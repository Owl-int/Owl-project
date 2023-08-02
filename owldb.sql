CREATE DATABASE IF NOT EXISTS owldb;
USE owldb;

-- Tabla Usuarios 1
CREATE TABLE Usuarios (
  id_usuario INT PRIMARY KEY auto_increment,
  nom_usuario VARCHAR(45),
  nombre VARCHAR(45), 
  ap_paterno VARCHAR(45),
  ap_materno VARCHAR(45),
  correo VARCHAR(45),
  passw VARCHAR(45)
);

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nom_usuario`, `nombre`, `ap_paterno`, `ap_materno`, `correo`, `passw`) VALUES
(1, 'carlitosonichan777', 'carlitos', 'esto es', 'una prueba', 'carlitosonichan777@gmail.com', 'ola');


-- Tabla Paciente 2
CREATE TABLE Paciente (
  id_paciente INT PRIMARY KEY auto_increment,
  registro_online VARCHAR(2), 
  id_usuario INT,
  nombre_cliente VARCHAR(45),
  ap_pa VARCHAR(45),
  ap_ma VARCHAR(45),
  fecha_nacimiento DATE, -- Calcular si es mayor de edad xd
  genero VARCHAR(10),
  estado_civil VARCHAR(10),
  contacto VARCHAR(10),
  antecedentes_medicos VARCHAR(255),
  medicamentos_actuales VARCHAR(255),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla Clinicas 3
CREATE TABLE Clinicas(
  id_clinica INT PRIMARY KEY auto_increment, 
  nombre VARCHAR(45), 
  descripcion VARCHAR(45), 
  direccion VARCHAR(45),
  num_tel VARCHAR (10)
); 


--
-- Volcado de datos para la tabla `clinicas`
--

INSERT INTO `clinicas` (`id_clinica`, `nombre`, `descripcion`, `direccion`, `num_tel`) VALUES
(1, 'Resilitente ', 'Institución independiente dedicada a la salud', 'Santa Anita', 2147483647),
(2, 'HOREM', 'Centro de salud publica', 'Centro', 2147483647),
(3, 'Agua Clara', 'Instutución mediocre y saturada y fea', 'Ciudad Satélite Morelos', 2147483647);


-- Tabla Profesional_encargado 4
CREATE TABLE Profesional_encargado (
  id_pro INT PRIMARY KEY auto_increment, 
  nom VARCHAR(45),                        
  ap VARCHAR(45),                        
  especialidad VARCHAR(45),              
  cedula_profesional VARCHAR(7),         
  num_telefono VARCHAR(10),                  
  correo_elec VARCHAR(45),               
  horario VARCHAR(10),                   
  nom_clinica VARCHAR(45)                  
);

--
-- Volcado de datos para la tabla `profesional_encargado`
--

INSERT INTO `profesional_encargado` (`id_pro`, `nom`, `ap`, `especialidad`, `cedula_profesional`, `num_telefono`, `correo_elec`, `horario`, `nom_clinica`) VALUES
(1, 'Yolanda ', 'Esparza', 'Psicologa', '1234567', 2147483647, 'ejemplo@gmail.com', 'MIX', 'Resilitente '),
(2, 'Alejandro', 'Diaz', 'Psicologo', '1234568', 2147483647, 'ejemplo2@gmail.com', 'MIX', 'HOREM'),
(4, 'Tontuelo', 'Fernandez', 'Psiquiatra', '1234567', 2147483647, 'ejemplo2@gmail.com', 'MIX', 'Agua Clara');


-- Tabla Horario 5
CREATE TABLE Horario (
  id_horario VARCHAR(3) PRIMARY KEY,
  desc_horario VARCHAR(255)
);

--
-- Volcado de datos para la tabla `horario`
--
INSERT INTO `horario` (`id_horario`, `desc_horario`) VALUES
('MAT', 'Matutino'),
('MIX', 'Mixto'),
('VES', 'Vespertino');

-- Tabla Citas 6
CREATE TABLE Citas (
  id_cita INT PRIMARY KEY auto_increment,
  descripcion VARCHAR(255),
  fecha DATE,
  hora TIME,
  id_usuario INT,
  nom_paciente VARCHAR(45),
  nom_profesional VARCHAR(45),
  nom_clinica VARCHAR(45),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Tabla Historial_citas 7
CREATE TABLE Historial_citas (
  id_usuario INT, 
  id_paciente INT, 
  nombre_cliente VARCHAR(50),
  id_cita INT,
  fecha DATE,
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario), 
  FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
  FOREIGN KEY (id_cita) REFERENCES Citas(id_cita)
);
-- Contacto Emergencia 8
CREATE TABLE Contacto_emergencia(
  id_usuario INT,
  nombre_contacto VARCHAR(45),
  relacion_paciente VARCHAR(45),
  num_tel VARCHAR(10),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
); 


