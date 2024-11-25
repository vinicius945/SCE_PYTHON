CREATE TABLE avaliacao (
    id_avaliacao    NUMBER(10) NOT NULL,
    titulo          VARCHAR2(100 CHAR),
    nota            NUMBER(10),
    comentario      VARCHAR2(300 CHAR),
    data_avaliacao  DATE,
    id_cliente      NUMBER(10) NOT NULL,
    id_empresa      NUMBER(10) NOT NULL
);

ALTER TABLE avaliacao ADD CONSTRAINT avaliacao_pk PRIMARY KEY ( id_avaliacao );

CREATE TABLE cliente (
    id_cliente  NUMBER(10) NOT NULL,
    nome        VARCHAR2(100 CHAR),
    email       VARCHAR2(320 CHAR),
    genero      VARCHAR2(15 CHAR)
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE empresa (
    id_empresa  NUMBER(10) NOT NULL,
    nome        VARCHAR2(100 CHAR),
    cnpj        VARCHAR2(20 CHAR),
    vantagens   VARCHAR2(100 CHAR)
);

ALTER TABLE empresa ADD CONSTRAINT empresa_pk PRIMARY KEY ( id_empresa );

ALTER TABLE avaliacao
    ADD CONSTRAINT avaliacao_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE avaliacao
    ADD CONSTRAINT avaliacao_empresa_fk FOREIGN KEY ( id_empresa )
        REFERENCES empresa ( id_empresa );

CREATE OR REPLACE TRIGGER fkntm_avaliacao BEFORE
    UPDATE OF id_cliente, id_empresa ON avaliacao
BEGIN
    raise_application_error(-20225, 'Non Transferable FK constraint  on table AVALIACAO is violated');
END;