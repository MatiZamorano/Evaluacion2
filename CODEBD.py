CREATE TABLE alu_mod (
    alumno_idalumno INTEGER NOT NULL,
    modulo_idmodulo INTEGER NOT NULL
);

ALTER TABLE alu_mod ADD CONSTRAINT alu_mod_pk PRIMARY KEY ( alumno_idalumno,
                                                            modulo_idmodulo );

CREATE TABLE alu_sec (
    alumno_idalumno   INTEGER NOT NULL,
    seccion_idseccion INTEGER NOT NULL
);

ALTER TABLE alu_sec ADD CONSTRAINT alu_sec_pk PRIMARY KEY ( alumno_idalumno,
                                                            seccion_idseccion );

CREATE TABLE alumno (
    idalumno    INTEGER NOT NULL,
    tipousuario VARCHAR2(20) NOT NULL,
    nombres     VARCHAR2(50) NOT NULL,
    apellidop   VARCHAR2(25) NOT NULL,
    apellidom   VARCHAR2(25) NOT NULL,
    rut         VARCHAR2(12) NOT NULL,
    direccion   VARCHAR2(100) NOT NULL,
    comuna      VARCHAR2(25),
    cuidad      VARCHAR2(25) NOT NULL,
    telefono    INTEGER NOT NULL,
    correo      VARCHAR2(50) NOT NULL,
    usuario     VARCHAR2(25) NOT NULL,
    contraseña  VARCHAR2(25) NOT NULL,
    area        VARCHAR2(100) NOT NULL
);

ALTER TABLE alumno ADD CONSTRAINT alumno_pk PRIMARY KEY ( idalumno );

CREATE TABLE docente (
    iddocente        INTEGER NOT NULL,
    tipousuario      VARCHAR2(20) NOT NULL,
    nombres          VARCHAR2(50) NOT NULL,
    apellidop        VARCHAR2(25) NOT NULL,
    apellidom        VARCHAR2(25) NOT NULL,
    rut              VARCHAR2(12) NOT NULL,
    direccion        VARCHAR2(100) NOT NULL,
    comuna           VARCHAR2(25) NOT NULL,
    cuidad           VARCHAR2(25) NOT NULL,
    telefono         INTEGER NOT NULL,
    correo           VARCHAR2(50) NOT NULL,
    usuario          VARCHAR2(25) NOT NULL,
    contraseña       VARCHAR2(25) NOT NULL,
    jefecarrera_idjc INTEGER NOT NULL,
    area             VARCHAR2(100) NOT NULL
);

ALTER TABLE docente ADD CONSTRAINT docente_pk PRIMARY KEY ( iddocente,
                                                            jefecarrera_idjc );

CREATE TABLE jefecarrera (
    idjc        INTEGER NOT NULL,
    tipousuario VARCHAR2(20) NOT NULL,
    nombres     VARCHAR2(25) NOT NULL,
    apellidop   VARCHAR2(25) NOT NULL,
    apellidom   VARCHAR2(25) NOT NULL,
    comuna      VARCHAR2(25),
    cuidad      VARCHAR2(25),
    rut         VARCHAR2(12) NOT NULL,
    direccion   VARCHAR2(100) NOT NULL,
    telefono    INTEGER NOT NULL,
    correo      VARCHAR2(50) NOT NULL,
    usuario     VARCHAR2(25) NOT NULL,
    contraseña  VARCHAR2(25) NOT NULL,
    area        VARCHAR2(100) NOT NULL
);

ALTER TABLE jefecarrera ADD CONSTRAINT jefecarrera_pk PRIMARY KEY ( idjc );

CREATE TABLE matricula (
    idmatricula     INTEGER NOT NULL,
    folio           INTEGER NOT NULL,
    fechainscipcion DATE NOT NULL,
    cuota           INTEGER NOT NULL,
    semestre        VARCHAR2(25) NOT NULL,
    arancel         INTEGER NOT NULL,
    carrera         VARCHAR2(50) NOT NULL,
    sede            VARCHAR2(25) NOT NULL,
    alumno_idalumno INTEGER NOT NULL,
    rut             INTEGER NOT NULL,
    nombre          VARCHAR2(50) NOT NULL,
    apellidop       VARCHAR2(25) NOT NULL,
    apellidom       VARCHAR2(25) NOT NULL,
    direccion       VARCHAR2(50) NOT NULL,
    comuna          VARCHAR2(25) NOT NULL,
    cuidad          VARCHAR2(25) NOT NULL,
    telefono        INTEGER NOT NULL,
    estadopago      VARCHAR2(25) NOT NULL
);

ALTER TABLE matricula ADD CONSTRAINT matricula_pk PRIMARY KEY ( alumno_idalumno,
                                                                idmatricula );

CREATE TABLE mod_doc (
    docente_iddocente        INTEGER NOT NULL,
    docente_jefecarrera_idjc INTEGER NOT NULL,
    modulo_idmodulo          INTEGER NOT NULL
);

ALTER TABLE mod_doc
    ADD CONSTRAINT mod_doc_pk PRIMARY KEY ( docente_iddocente,
                                            docente_jefecarrera_idjc,
                                            modulo_idmodulo );

CREATE TABLE modulo (
    idmodulo     INTEGER NOT NULL,
    nombremodulo VARCHAR2(50) NOT NULL,
    nota         INTEGER
);

ALTER TABLE modulo ADD CONSTRAINT modulo_pk PRIMARY KEY ( idmodulo );

CREATE TABLE sec_jc (
    jefecarrera_idjc  INTEGER NOT NULL,
    seccion_idseccion INTEGER NOT NULL
);

ALTER TABLE sec_jc ADD CONSTRAINT sec_jc_pk PRIMARY KEY ( jefecarrera_idjc,
                                                          seccion_idseccion );

CREATE TABLE sec_mod (
    modulo_idmodulo   INTEGER NOT NULL,
    seccion_idseccion INTEGER NOT NULL
);

ALTER TABLE sec_mod ADD CONSTRAINT sec_mod_pk PRIMARY KEY ( modulo_idmodulo,
                                                            seccion_idseccion );

CREATE TABLE seccion (
    idseccion     INTEGER NOT NULL,
    nombreseccion VARCHAR2(50) NOT NULL,
    modalidad     VARCHAR2(25) NOT NULL,
    area          VARCHAR2(100) NOT NULL
);

ALTER TABLE seccion ADD CONSTRAINT seccion_pk PRIMARY KEY ( idseccion );

ALTER TABLE alu_mod
    ADD CONSTRAINT alu_mod_alumno_fk FOREIGN KEY ( alumno_idalumno )
        REFERENCES alumno ( idalumno );

ALTER TABLE alu_mod
    ADD CONSTRAINT alu_mod_modulo_fk FOREIGN KEY ( modulo_idmodulo )
        REFERENCES modulo ( idmodulo );

ALTER TABLE alu_sec
    ADD CONSTRAINT alu_sec_alumno_fk FOREIGN KEY ( alumno_idalumno )
        REFERENCES alumno ( idalumno );

ALTER TABLE alu_sec
    ADD CONSTRAINT alu_sec_seccion_fk FOREIGN KEY ( seccion_idseccion )
        REFERENCES seccion ( idseccion );

ALTER TABLE docente
    ADD CONSTRAINT docente_jefecarrera_fk FOREIGN KEY ( jefecarrera_idjc )
        REFERENCES jefecarrera ( idjc );

ALTER TABLE matricula
    ADD CONSTRAINT matricula_alumno_fk FOREIGN KEY ( alumno_idalumno )
        REFERENCES alumno ( idalumno );

ALTER TABLE mod_doc
    ADD CONSTRAINT mod_doc_docente_fk FOREIGN KEY ( docente_iddocente,
                                                    docente_jefecarrera_idjc )
        REFERENCES docente ( iddocente,
                             jefecarrera_idjc );

ALTER TABLE mod_doc
    ADD CONSTRAINT mod_doc_modulo_fk FOREIGN KEY ( modulo_idmodulo )
        REFERENCES modulo ( idmodulo );

ALTER TABLE sec_jc
    ADD CONSTRAINT sec_jc_jefecarrera_fk FOREIGN KEY ( jefecarrera_idjc )
        REFERENCES jefecarrera ( idjc );

ALTER TABLE sec_jc
    ADD CONSTRAINT sec_jc_seccion_fk FOREIGN KEY ( seccion_idseccion )
        REFERENCES seccion ( idseccion );

ALTER TABLE sec_mod
    ADD CONSTRAINT sec_mod_modulo_fk FOREIGN KEY ( modulo_idmodulo )
        REFERENCES modulo ( idmodulo );

ALTER TABLE sec_mod
    ADD CONSTRAINT sec_mod_seccion_fk FOREIGN KEY ( seccion_idseccion )
        REFERENCES seccion ( idseccion );

CREATE SEQUENCE alumno_idalumno_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER alumno_idalumno_trg BEFORE
    INSERT ON alumno
    FOR EACH ROW
    WHEN ( new.idalumno IS NULL )
BEGIN
    :new.idalumno := alumno_idalumno_seq.nextval;
END;
/

CREATE SEQUENCE docente_iddocente_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER docente_iddocente_trg BEFORE
    INSERT ON docente
    FOR EACH ROW
    WHEN ( new.iddocente IS NULL )
BEGIN
    :new.iddocente := docente_iddocente_seq.nextval;
END;
/

CREATE SEQUENCE jefecarrera_idjc_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER jefecarrera_idjc_trg BEFORE
    INSERT ON jefecarrera
    FOR EACH ROW
    WHEN ( new.idjc IS NULL )
BEGIN
    :new.idjc := jefecarrera_idjc_seq.nextval;
END;
/

CREATE SEQUENCE matricula_idmatricula_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER matricula_idmatricula_trg BEFORE
    INSERT ON matricula
    FOR EACH ROW
    WHEN ( new.idmatricula IS NULL )
BEGIN
    :new.idmatricula := matricula_idmatricula_seq.nextval;
END;
/

CREATE SEQUENCE matricula_folio_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER matricula_folio_trg BEFORE
    INSERT ON matricula
    FOR EACH ROW
    WHEN ( new.folio IS NULL )
BEGIN
    :new.folio := matricula_folio_seq.nextval;
END;
/

CREATE SEQUENCE modulo_idmodulo_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER modulo_idmodulo_trg BEFORE
    INSERT ON modulo
    FOR EACH ROW
    WHEN ( new.idmodulo IS NULL )
BEGIN
    :new.idmodulo := modulo_idmodulo_seq.nextval;
END;
/

CREATE SEQUENCE seccion_idseccion_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER seccion_idseccion_trg BEFORE
    INSERT ON seccion
    FOR EACH ROW
    WHEN ( new.idseccion IS NULL )
BEGIN
    :new.idseccion := seccion_idseccion_seq.nextval;
END;
/
