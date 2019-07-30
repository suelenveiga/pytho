CREATE TABLE "Serie" (
    "titulo" varchar(100) NOT NULL,
    "codigo" serial unique,

    CONSTRAINT "SeriePK" PRIMARY KEY ("codigo")
)


CREATE TABLE "Temporada" (
    "descricao" varchar (100) NOT NULL,
    "codigo" serial unique,
    "FK_serie_cod" serial unique,
    "numero" int NOT NULL,
    CONSTRAINT "TemporadaPK" PRIMARY KEY ("codigo"),
    CONSTRAINT "SeriecodFK" FOREIGN KEY ("FK_serie_cod")
        REFERENCES "Serie" ("codigo")
            ON DELETE SET NOT NULL
            ON UPDATE CASCADE  
)

CREATE TABLE "Episodio" (
    "titulo" varchar (100) NOT NULL,
    "codigo" serial unique,
    "numero" int NOT NULL,
    "FK_serie_cod" serial unique,
    "FK_temporada_cod" serial unique,
    CONSTRAINT "EpisodioPK" PRIMARY KEY ("codigo"),
    CONSTRAINT "FK_serie_cod" FOREIGN KEY ("FK_serie_cod")
        REFERENCES "Serie" ("codigo")
            ON DELETE SET NOT NULL
            ON UPDATE CASCADE ,
    CONSTRAINT "FK_temporada_cod" FOREIGN KEY ("FK_temporada_cod")
        REFERENCES "Temporada" ("codigo")
            ON DELETE SET NOT NULL
            ON UPDATE CASCADE  
)

CREATE TABLE "Usuario" (
    "nome" varchar (100) NOT NULL,
    "codserie" int NOT NULL,
    "login" varchar (100) NOT NULL,
    "altura" float NOT NULL,
    "idade" int NOT NULL,
    "email" varchar (100) unique,
    "senha" varchar (8) NOT NULL,
    CONSTRAINT "UsuarioPK" PRIMARY KEY ("email"),
    CONSTRAINT "codserieFK" FOREIGN KEY ("codserie")
        REFERENCES "Serie" ("codigo")
            ON DELETE SET NULL
            ON UPDATE set null
)