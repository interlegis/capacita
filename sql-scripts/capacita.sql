--
-- File generated with SQLiteStudio v3.1.1 on sex ago 31 09:28:25 2018
--
-- Text encoding used: UTF-8
--
-- PRAGMA foreign_keys = off;
-- BEGIN TRANSACTION;

-- Table: Area_Conhecimento
CREATE TABLE Area_Conhecimento (
    cod_area_conhecimento SERIAL PRIMARY KEY,
    txt_descricao         VARCHAR (200) NOT NULL,
    ind_excluido          DECIMAL       NOT NULL
);

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  266,
                                  'Comunicaçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  292,
                                  'Ciencia da Computaçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  294,
                                  'Direito',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  295,
                                  'Administraçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  296,
                                  'Economia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  297,
                                  'Demografia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  299,
                                  'Ciencia da Informaçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  300,
                                  'Serviço Social',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  301,
                                  'Sociologia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  302,
                                  'Antropologia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  303,
                                  'Arqueologia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  304,
                                  'Geografia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  305,
                                  'Ciencia Politica ',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  306,
                                  'Matematica',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  307,
                                  'Probabilidade e Estatistica',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  308,
                                  'Ciencias Biologicas',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  309,
                                  'Engenharias',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  310,
                                  'Ciencias da Saude',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  311,
                                  'Arquitetura',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  312,
                                  'Ciencia da Informaçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  313,
                                  'Ciencias Humanas',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  314,
                                  'Psicologia',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  315,
                                  'Educaçao',
                                  0
                              );

INSERT INTO Area_Conhecimento (
                                  cod_area_conhecimento,
                                  txt_descricao,
                                  ind_excluido
                              )
                              VALUES (
                                  316,
                                  'Letras',
                                  0
                              );

-- Table: Iniciativa
CREATE TABLE Iniciativa (
    cod_iniciativa SERIAL PRIMARY KEY,
    nome           VARCHAR (200) NOT NULL
);

INSERT INTO Iniciativa (
                           cod_iniciativa,
                           nome
                       )
                       VALUES (
                           1,
                           'iniciativa1'
                       );


-- Table: Mes
CREATE TABLE Mes (
    cod_mes SERIAL PRIMARY KEY,
    nome    VARCHAR (200) NOT NULL
);

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    1,
                    'Janeiro'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    2,
                    'Fevereiro'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    3,
                    'Março'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    4,
                    'Abril'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    5,
                    'Maio'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    6,
                    'Junho'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    7,
                    'Julho'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    8,
                    'Agosto'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    9,
                    'Setembro'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    10,
                    'Outubro'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    11,
                    'Novembro'
                );

INSERT INTO Mes (
                    cod_mes,
                    nome
                )
                VALUES (
                    12,
                    'Dezembro'
                );

-- Table: 
CREATE TABLE Nivel (
    cod_nivel SERIAL PRIMARY KEY,
    nome      VARCHAR (200) NOT NULL
);


-- Table: Orgao
CREATE TABLE Orgao (
    cod_orgao SERIAL PRIMARY KEY,
    nome      VARCHAR (200) NOT NULL
);

-- Table: Tipo_Plano_Capacitacao
CREATE TABLE Tipo_Plano_Capacitacao (
    cod_tipo_plano_capacitacao  SERIAL PRIMARY KEY,
    sgl_tipo_plano_capacitacao  VARCHAR (6)   NOT NULL,
    ind_excluido                DECIMAL       NOT NULL,
    nome_tipo_plano_capacitacao VARCHAR (200) NOT NULL
);

-- Table: Plano_Capacitacao
CREATE TABLE Plano_Capacitacao (
    cod_plano_capacitacao         SERIAL PRIMARY KEY,
    ano_plano_capacitacao         DECIMAL       NOT NULL,
    ind_excluido                  DECIMAL       NOT NULL,
    cod_orgao_id                  INTEGER       NOT NULL
                                                REFERENCES Orgao (cod_orgao) DEFERRABLE INITIALLY DEFERRED,
    cod_tipo_plano_capacitacao_id INTEGER       NOT NULL
                                                REFERENCES Tipo_Plano_Capacitacao (cod_tipo_plano_capacitacao) DEFERRABLE INITIALLY DEFERRED,
    qtd_servidores_comissionados  INTEGER       NOT NULL,
    qtd_servidores_efetivos       INTEGER       NOT NULL,
    situacao                      VARCHAR (200) NOT NULL
);


-- Table: Turno
CREATE TABLE Turno (
    cod_turno SERIAL PRIMARY KEY,
    nome      VARCHAR (200) NOT NULL
);

-- Table: Prioridade
CREATE TABLE Prioridade (
    cod_prioridade SERIAL PRIMARY KEY,
    nome           VARCHAR (200) NOT NULL
);

-- Table: Sub_Area_Conhecimento
CREATE TABLE Sub_Area_Conhecimento (
    cod_sub_area_conhecimento SERIAL PRIMARY KEY,
    txt_descricao             VARCHAR (200) NOT NULL,
    ind_excluido              DECIMAL       NOT NULL,
    cod_area_conhecimento_id  INTEGER       NOT NULL
                                            REFERENCES Area_Conhecimento (cod_area_conhecimento) DEFERRABLE INITIALLY DEFERRED
);

-- Table: Necessidade
CREATE TABLE Necessidade (
    cod_necessidade              SERIAL PRIMARY KEY,
    txt_descricao                VARCHAR (200) NOT NULL,
    qtd_servidor                 DECIMAL       NOT NULL,
    hor_duracao                  DECIMAL       NOT NULL,
    ind_excluido                 DECIMAL       NOT NULL,
    cod_iniciativa_id            INTEGER       NOT NULL
                                               REFERENCES Iniciativa (cod_iniciativa),
    cod_mes_id                   INTEGER       NOT NULL
                                               REFERENCES Mes (cod_mes),
    cod_nivel_id                 INTEGER       NOT NULL
                                               REFERENCES Nivel (cod_nivel),
    cod_plano_capacitacao_id     INTEGER       NOT NULL
                                               REFERENCES Plano_Capacitacao (cod_plano_capacitacao),
    cod_prioridade_id            INTEGER       NOT NULL
                                               REFERENCES Prioridade (cod_prioridade),
    cod_turno_id                 INTEGER       NOT NULL
                                               REFERENCES Turno (cod_turno),
    cod_sub_area_conhecimento_id INTEGER       NOT NULL
                                               REFERENCES Sub_Area_Conhecimento (cod_sub_area_conhecimento) 
);
						

-- Table: Avaliacao
CREATE TABLE Avaliacao (
    cod_avaliacao      SERIAL PRIMARY KEY,
    valor_custo        DECIMAL NOT NULL,
    ind_excluido       DECIMAL NOT NULL,
    cod_necessidade_id INTEGER NOT NULL
                               REFERENCES Necessidade (cod_necessidade) DEFERRABLE INITIALLY DEFERRED
);



INSERT INTO Nivel (
                      cod_nivel,
                      nome
                  )
                  VALUES (
                      1,
                      'nivel'
                  );



INSERT INTO Orgao (
                      cod_orgao,
                      nome
                  )
                  VALUES (
                      2,
                      'Orgao2'
                  );

INSERT INTO Orgao (
                      cod_orgao,
                      nome
                  )
                  VALUES (
                      4,
                      'teste de orgao'
                  );

-- Table: Secretaria
CREATE TABLE Secretaria (
    cod_secretaria SERIAL PRIMARY KEY,
    nome           VARCHAR (200) NOT NULL
);

-- Table: Permissao
CREATE TABLE Permissao (
    cod_permissao                 SERIAL PRIMARY KEY,
    ano_plano_capacitacao         DECIMAL NOT NULL,
    cod_secretaria_id             INTEGER NOT NULL
                                          REFERENCES Secretaria (cod_secretaria) DEFERRABLE INITIALLY DEFERRED,
    cod_tipo_plano_capacitacao_id INTEGER NOT NULL
                                          REFERENCES Tipo_Plano_Capacitacao (cod_tipo_plano_capacitacao) DEFERRABLE INITIALLY DEFERRED
);


INSERT INTO Plano_Capacitacao (
                                  cod_plano_capacitacao,
                                  ano_plano_capacitacao,
                                  ind_excluido,
                                  cod_orgao_id,
                                  cod_tipo_plano_capacitacao_id,
                                  qtd_servidores_comissionados,
                                  qtd_servidores_efetivos,
                                  situacao
                              )
                              VALUES (
                                  6,
                                  218,
                                  0,
                                  2,
                                  1,
                                  222,
                                  212,
                                  'alskdf'
                              );

INSERT INTO Plano_Capacitacao (
                                  cod_plano_capacitacao,
                                  ano_plano_capacitacao,
                                  ind_excluido,
                                  cod_orgao_id,
                                  cod_tipo_plano_capacitacao_id,
                                  qtd_servidores_comissionados,
                                  qtd_servidores_efetivos,
                                  situacao
                              )
                              VALUES (
                                  7,
                                  2019,
                                  0,
                                  4,
                                  1,
                                  12,
                                  22,
                                  'toughth'
                              );
INSERT INTO Prioridade (
                           cod_prioridade,
                           nome
                       )
                       VALUES (
                           1,
                           'prioridade'
                       );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      234,
                                      'Distribuição Espacial',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      235,
                                      'Tendência Populacional',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      236,
                                      'Componentes da Dinâmica Demográfica',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      237,
                                      'Nupcialidade e Família',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      238,
                                      'Demografia Histórica',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      239,
                                      'Política Pública e População',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      240,
                                      'Fontes de Dados Demográficos',
                                      0,
                                      297
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      258,
                                      'Teoria da Informaçao',
                                      0,
                                      299
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      259,
                                      'Biblioteconomia',
                                      0,
                                      299
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      260,
                                      'Arquivologia',
                                      0,
                                      299
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      261,
                                      'Fundamentos do Serviço Social',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      263,
                                      'Fundamentos da Sociologia',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      264,
                                      'Sociologia do Conhecimento',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      265,
                                      'Sociologia do Desenvolvimento',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      266,
                                      'Sociologia Urbana',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      267,
                                      'Sociologia Rural',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      268,
                                      'Sociologia da Saude',
                                      0,
                                      301
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      269,
                                      'Teoria Antropologica',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      270,
                                      'Etnologia Indigena',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      271,
                                      'Antropologia Urbana',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      272,
                                      'Antropologia Rural',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      273,
                                      'Sociologia Rural',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      274,
                                      'Antropologia das Populações Afro-Brasileiras',
                                      0,
                                      302
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      275,
                                      'Teoria e Método em Arqueologia',
                                      0,
                                      303
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      276,
                                      'Arqueologia Pré-Histórica',
                                      0,
                                      303
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      277,
                                      'Arqueologia Histórica',
                                      0,
                                      303
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      278,
                                      'Geografia Humana',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      279,
                                      'Geografia Regional',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      280,
                                      'Teoria Politica',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      281,
                                      'Estado e Governo',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      282,
                                      'Comportamento Politico',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      283,
                                      'Politicas Publicas',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      284,
                                      'Politica Internacional',
                                      0,
                                      304
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      285,
                                      'Algebra',
                                      0,
                                      306
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      286,
                                      'Analise',
                                      0,
                                      306
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      287,
                                      'Geometria e Topologia',
                                      0,
                                      306
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      288,
                                      'Matematica Aplicada',
                                      0,
                                      306
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      289,
                                      'Probabilidade',
                                      0,
                                      307
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      290,
                                      'Estatistica',
                                      0,
                                      307
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      291,
                                      'Probabilidade e Estatistica Aplicada',
                                      0,
                                      307
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      292,
                                      'Computabilidade e Modelos de Computação',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      293,
                                      'Linguagem Formais e Automatos',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      294,
                                      'Análise de Algoritmos e Complexidade de Computação',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      295,
                                      'Lógicas e Semântica de Programas',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      296,
                                      'Matemática Simbólica',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      297,
                                      ' Modelos Analíticos e de Simulação',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      298,
                                      'Linguagens de Programação',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      299,
                                      'Engenharia de Software',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      300,
                                      'Banco de Dados',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      301,
                                      'Sistemas de Informaçãos',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      302,
                                      'Banco de Dados',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      303,
                                      ' Processamento Gráfico (Graphics)',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      304,
                                      'Hardware',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      305,
                                      'Arquitetura de Sistemas de Computação',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      306,
                                      'Software Básico',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      307,
                                      'Teleinformática',
                                      0,
                                      292
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      308,
                                      'Biologia Geral',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      309,
                                      'Genética',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      310,
                                      'Botânica',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      311,
                                      'Zoologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      312,
                                      'Ecologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      313,
                                      'Morfologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      314,
                                      'Fisiologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      315,
                                      'Bioquímica',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      316,
                                      'Biofísica',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      317,
                                      'Farmacologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      318,
                                      'Imunologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      319,
                                      'Microbiologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      320,
                                      'Parasitologia',
                                      0,
                                      308
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      321,
                                      'Engenharia Civil',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      322,
                                      'Engenharia de Minas',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      323,
                                      'Engenharia de Materiais e Metalúrgica',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      324,
                                      'Engenharia Elétrica',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      325,
                                      'Engenharia Mecânica',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      326,
                                      'Engenharia Química',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      327,
                                      'Engenharia Sanitária',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      328,
                                      'Engenharia de Produção',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      329,
                                      'Engenharia Nuclear',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      330,
                                      'Engenharia de Transportes',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      331,
                                      'Engenharia Biomédica',
                                      0,
                                      309
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      332,
                                      'Medicina',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      333,
                                      'Odontologia',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      334,
                                      'Farmacia',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      335,
                                      'Enfermagem',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      336,
                                      'Nutriçao',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      337,
                                      'Saude Coletiva',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      338,
                                      'Fonoaudiologia',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      339,
                                      'Fisioterapia e Terapia Ocupacional',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      340,
                                      'Educação Física',
                                      0,
                                      310
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      341,
                                      'Teoria Geral do Direito',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      342,
                                      'Teoria Geral do Processo',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      343,
                                      'Teoria do Estado',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      344,
                                      'História do Direito',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      345,
                                      'Filosofia do Direito',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      346,
                                      'Lógica Jurídica',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      347,
                                      'Sociologia Jurídica',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      348,
                                      'Antropologia Jurídica',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      349,
                                      'Direito Tributário',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      350,
                                      'Direito Penal',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      351,
                                      'Direito Processual Penal',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      352,
                                      'Direito Processual Civil',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      353,
                                      'Direito Constitucional',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      354,
                                      'Direito Administrativo',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      355,
                                      'Direito Internacional Público',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      356,
                                      'Direito Civil',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      357,
                                      'Direito Comercial',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      358,
                                      'Direito do Trabalho',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      359,
                                      'Direito Internacional Privado',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      360,
                                      'Direitos Especiais',
                                      0,
                                      294
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      361,
                                      'Administração da Produção',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      362,
                                      'Administração Financeira',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      363,
                                      'Mercadologia',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      364,
                                      'Negócios Internacionais',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      365,
                                      'Administração de Recursos Humanos',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      366,
                                      'Contabilidade e Financas Públicas',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      367,
                                      'Organizações Públicas',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      368,
                                      'Política e Planejamento Governamentais',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      369,
                                      'Administração de Pessoal',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      370,
                                      'Administração de Setores Específicos',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      371,
                                      'Ciências Contábeis',
                                      0,
                                      295
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      372,
                                      'Economia Geral',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      373,
                                      'Teoria Geral da Economia',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      374,
                                      'História do Pensamento Econômico',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      375,
                                      'História Econômica',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      376,
                                      'Sistemas Econômicos',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      377,
                                      'Métodos e Modelos Matemáticos, Econométricos e Estatísticos',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      378,
                                      'Estatística Sócio-Econômica',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      379,
                                      'Contabilidade Nacional',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      380,
                                      'Economia Matemática',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      381,
                                      ' Teoria Monetária e Financeira',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      382,
                                      'Instituições Monetárias e Financeiras do Brasil',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      383,
                                      'Financas Públicas Internas',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      384,
                                      'Política Fiscal do Brasil',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      385,
                                      'Crescimento e Desenvolvimento Econômico',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      386,
                                      'Teoria e Política de Planejamento Econômico',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      387,
                                      ' Flutuações Cíclicas e Projeções Econômicas',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      388,
                                      'Inflação',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      389,
                                      'Teoria do Comércio Internacional',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      390,
                                      'Relações do Comércio; Política Comercial; Integração Econômica',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      391,
                                      'Balanço de Pagamentos; Financas Internacionais',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      392,
                                      'Treinamento e Alocação de Mão-de-Obra; Oferta de Mão-de-Obra e Força de Trabalho',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      393,
                                      'Mercado de Trabalho; Política do Governo',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      394,
                                      'Sindicatos, Dissídios Coletivos, Relações de Emprego (Empregador/Empregado)',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      395,
                                      'Capital Humano',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      396,
                                      'Demografia Econômica',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      397,
                                      'Organização Industrial e Estudos Industriais',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      398,
                                      'Mudança Tecnologica',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      399,
                                      'Economia dos Programas de Bem-Estar Socia',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      400,
                                      'Economia do Consumidor',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      401,
                                      'Economia Regional',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      402,
                                      'Economia Urbana',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      403,
                                      'Renda e Tributação',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      404,
                                      'Economia Agrária',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      405,
                                      'Economia dos Recursos Naturais',
                                      0,
                                      296
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      406,
                                      'Fundamentos de Arquitetura e Urbanismo',
                                      0,
                                      311
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      407,
                                      'Projeto de Arquitetuta e Urbanismo',
                                      0,
                                      311
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      408,
                                      'Tecnologia de Arquitetura e Urbanismo',
                                      0,
                                      311
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      409,
                                      'Paisagismo',
                                      0,
                                      311
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      410,
                                      'Teoria Geral da Informação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      411,
                                      'Processos da Comunicação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      412,
                                      'Representação da Informação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      413,
                                      'Teoria da Classificação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      414,
                                      'Métodos Quantitativos. Bibliometria',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      415,
                                      'Técnicas de Recuperação de Informação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      416,
                                      'Processos de Disseminação da Informação',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      417,
                                      'Organização de Arquivos',
                                      0,
                                      312
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      418,
                                      'Teoria da Comunicação',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      419,
                                      'Teoria e Ética do Jornalismo',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      420,
                                      'Organização Editorial de Jornais',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      421,
                                      'Organização Comercial de Jornais',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      422,
                                      'Jornalismo Especializado (Comunitário, Rural, Empresarial, Científico)',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      423,
                                      'Radiodifusão',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      424,
                                      'Videodifusão',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      425,
                                      'Relações Públicas e Propaganda',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      426,
                                      'Comunicação Visual',
                                      0,
                                      266
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      427,
                                      'Serviço Social do Trabalho',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      428,
                                      'Serviço Social da Educação',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      429,
                                      'Serviço Social do Menor',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      430,
                                      'Serviço Social da Saúde',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      431,
                                      'Serviço Social da Habitação',
                                      0,
                                      300
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      432,
                                      'Filosofia',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      433,
                                      'Sociologia',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      434,
                                      'Antropologia',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      435,
                                      'Arqueologia',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      436,
                                      'História',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      437,
                                      'Geografia',
                                      0,
                                      313
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      438,
                                      'Fundamentos e Medidas da Psicologia',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      439,
                                      'Psicologia Experimental',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      440,
                                      'Psicologia Fisiológica',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      441,
                                      'Psicologia Comparativa',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      442,
                                      'Psicologia Social',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      443,
                                      'Psicologia Cognitiva',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      444,
                                      'Psicologia do Desenvolvimento Humano',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      445,
                                      'Psicologia do Ensino e da Aprendizagem',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      446,
                                      'Psicologia do Trabalho e Organizacional',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      447,
                                      'Tratamento e Prevenção Psicológica',
                                      0,
                                      314
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      448,
                                      'Filosofia da Educação',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      449,
                                      'História da Educação',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      450,
                                      'Sociologia da Educação',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      451,
                                      'Antropologia Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      452,
                                      'Economia da Educação',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      453,
                                      'Psicologia Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      454,
                                      'Administração de Sistemas Educacionais',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      455,
                                      'Administração de Unidades Educativas',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      456,
                                      'Política Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      457,
                                      'Planejamento Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      458,
                                      'Avaliação de Sistemas, Instituições, Planos e Programas Educacionais',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      459,
                                      'Teorias da Instrução',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      460,
                                      'Métodos e Técnicas de Ensino',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      461,
                                      'Tecnologia Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      462,
                                      'Avaliação da Aprendizagem',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      463,
                                      'Teoria Geral de Planejamento e Desenvolvimento Curricular',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      464,
                                      'Currículos Específicos para Níveis e Tipos de Educação',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      465,
                                      'Orientação Educacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      466,
                                      'Orientação Vocacional',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      467,
                                      'Educação de Adultos',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      468,
                                      'Educação Permanente',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      469,
                                      'Educação Rural',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      470,
                                      'Educação em Periferias Urbanas',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      471,
                                      'Educação Especial',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      472,
                                      'Educação Pré-Escolar',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      473,
                                      'Ensino Profissionalizante',
                                      0,
                                      315
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      474,
                                      'Teoria Política Clássica',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      475,
                                      'Teoria Política Medieval',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      476,
                                      'Teoria Política Moderna',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      477,
                                      'Teoria Política Contemporânea',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      478,
                                      'Estrutura e Transformação do Estado',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      479,
                                      'Sistemas Governamentais Comparados',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      480,
                                      'Relações Intergovernamentais',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      481,
                                      'Estudos do Poder Local',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      482,
                                      'Instituições Governamentais Específicas',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      483,
                                      'Estudos Eleitorais e Partidos Políticos',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      484,
                                      'Atitude e Ideologias Políticas',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      485,
                                      'Conflitos e Coalizões Políticas',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      486,
                                      'Comportamento Legislativo',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      487,
                                      'Classes Sociais e Grupos de Interesse',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      488,
                                      'Análise do Processo Decisório',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      489,
                                      'Análise Institucional',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      490,
                                      'Técnicas de Antecipação',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      491,
                                      'Política Externa do Brasil',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      492,
                                      'Organizações Internacionais',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      493,
                                      'Integração Internacional, Conflito, Guerra e Paz',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      494,
                                      'Relações Internacionais, Bilaterais e Multilaterais',
                                      0,
                                      305
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      495,
                                      'Portugues',
                                      0,
                                      316
                                  );

INSERT INTO Sub_Area_Conhecimento (
                                      cod_sub_area_conhecimento,
                                      txt_descricao,
                                      ind_excluido,
                                      cod_area_conhecimento_id
                                  )
                                  VALUES (
                                      496,
                                      'Ingles',
                                      0,
                                      316
                                  );


INSERT INTO Tipo_Plano_Capacitacao (
                                       cod_tipo_plano_capacitacao,
                                       sgl_tipo_plano_capacitacao,
                                       ind_excluido,
                                       nome_tipo_plano_capacitacao
                                   )
                                   VALUES (
                                       1,
                                       'DPKG',
                                       0,
                                       'Tipo1_dpkg'
                                   );


INSERT INTO Turno (
                      cod_turno,
                      nome
                  )
                  VALUES (
                      1,
                      'Matutino'
                  );

INSERT INTO Turno (
                      cod_turno,
                      nome
                  )
                  VALUES (
                      2,
                      'Vespertino'
                  );

-- Index: Avaliacao_cod_necessidade_id_742d343f
-- CREATE INDEX Avaliacao_cod_necessidade_id_742d343f ON Avaliacao (
--     "cod_necessidade_id"
-- );

-- -- Index: Necessidade_014f539d
-- CREATE INDEX Necessidade_014f539d ON Necessidade (
--     "cod_iniciativa_id"
-- );


-- -- Index: Necessidade_1cbb3176
-- CREATE INDEX Necessidade_1cbb3176 ON Necessidade (
--     "cod_sub_area_conhecimento_id"
-- );


-- -- Index: Necessidade_3fffd84b
-- CREATE INDEX Necessidade_3fffd84b ON Necessidade (
--     "cod_nivel_id"
-- );


-- -- Index: Necessidade_51882d41
-- CREATE INDEX Necessidade_51882d41 ON Necessidade (
--     "cod_prioridade_id"
-- );


-- -- Index: Necessidade_a8243d73
-- CREATE INDEX Necessidade_a8243d73 ON Necessidade (
--     "cod_mes_id"
-- );


-- -- Index: Necessidade_b4a5eb0b
-- CREATE INDEX Necessidade_b4a5eb0b ON Necessidade (
--     "cod_turno_id"
-- );


-- -- Index: Necessidade_c2774db5
-- CREATE INDEX Necessidade_c2774db5 ON Necessidade (
--     "cod_plano_capacitacao_id"
-- );


-- -- Index: Permissao_cod_secretaria_id_8319a438
-- CREATE INDEX Permissao_cod_secretaria_id_8319a438 ON Permissao (
--     "cod_secretaria_id"
-- );


-- -- Index: Permissao_cod_tipo_plano_capacitacao_id_a1eb87aa
-- CREATE INDEX Permissao_cod_tipo_plano_capacitacao_id_a1eb87aa ON Permissao (
--     "cod_tipo_plano_capacitacao_id"
-- );


-- -- Index: Plano_Capacitacao_cod_orgao_id_e7b4bad6
-- CREATE INDEX Plano_Capacitacao_cod_orgao_id_e7b4bad6 ON Plano_Capacitacao (
--     "cod_orgao_id"
-- );


-- -- Index: Plano_Capacitacao_cod_tipo_plano_capacitacao_id_873b5a02
-- CREATE INDEX Plano_Capacitacao_cod_tipo_plano_capacitacao_id_873b5a02 ON Plano_Capacitacao (
--     "cod_tipo_plano_capacitacao_id"
-- );


-- -- Index: Sub_Area_Conhecimento_cod_area_conhecimento_id_e78cb2c3
-- CREATE INDEX Sub_Area_Conhecimento_cod_area_conhecimento_id_e78cb2c3 ON Sub_Area_Conhecimento (
--     cod_area_conhecimento_id
-- );


-- COMMIT TRANSACTION;
-- PRAGMA foreign_keys = on;
