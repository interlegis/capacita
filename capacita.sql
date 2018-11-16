DO
$do$
BEGIN
IF EXISTS (SELECT 1
   FROM   information_schema.tables
   WHERE  table_schema = 'public'
   AND    table_name = 'Area_Conhecimento') THEN
   RETURN;
ELSE

CREATE TABLE "Iniciativa" (
    cod_iniciativa SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Mes" (
    cod_mes SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Nivel" (
    cod_nivel SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Orgao" (
    cod_orgao SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Tipo_Plano_Capacitacao" (
    cod_tipo_plano_capacitacao SERIAL PRIMARY KEY,
    sgl_tipo_plano_capacitacao character varying(6) NOT NULL,
    nome_tipo_plano_capacitacao character varying(200) NOT NULL,
    ind_excluido numeric(2,0)
);


CREATE TABLE "Turno" (
    cod_turno SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Area_Conhecimento" (
    cod_area_conhecimento SERIAL PRIMARY KEY,
    txt_descricao character varying(200) NOT NULL,
    ind_excluido numeric(2,0) NOT NULL
);

CREATE TABLE "Treinamento" (
    cod_treinamento SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL,
    cod_area_conhecimento_id integer references "Area_Conhecimento"(cod_area_conhecimento)

);

-- CREATE TABLE "Treinamento" (
--     cod_treinamento SERIAL PRIMARY KEY,
--     txt_descricao character varying(200) NOT NULL,
--     ind_excluido numeric(2,0) NOT NULL,
--     cod_area_conhecimento_id integer references "Area_Conhecimento"(cod_area_conhecimento)
-- );

CREATE TABLE "Prioridade" (
    cod_prioridade SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Plano_Capacitacao" (
    cod_plano_capacitacao SERIAL PRIMARY KEY,
    nome character varying(200),
    situacao character varying(200) NOT NULL,
    qtd_servidores_efetivos integer NOT NULL,
    qtd_servidores_comissionados integer NOT NULL,
    ano_plano_capacitacao numeric(4,0) NOT NULL,
    ind_excluido numeric(2,0),
    cod_orgao_id integer references "Orgao"(cod_orgao),
    cod_tipo_plano_capacitacao_id integer references "Tipo_Plano_Capacitacao"(cod_tipo_plano_capacitacao)
);

insert into "Plano_Capacitacao" (cod_plano_capacitacao, nome, situacao, qtd_servidores_efetivos, qtd_servidores_comissionados,ano_plano_capacitacao, ind_excluido, cod_orgao_id, cod_tipo_plano_capacitacao_id) values (5, null, 'sim', 100, 500, 2019, null, null, null);


CREATE TABLE "Necessidade" (
    cod_necessidade SERIAL PRIMARY KEY,
    txt_descricao character varying(200) NOT NULL,
    qtd_servidor numeric(6,0) NOT NULL,
    hor_duracao numeric(2,0) NOT NULL,
    ind_excluido numeric(2,0) NOT NULL,
    cod_iniciativa_id integer references "Iniciativa"(cod_iniciativa),
    cod_mes_id integer references "Mes"(cod_mes),
    cod_nivel_id integer references "Nivel"(cod_nivel),
    cod_plano_capacitacao_id integer references "Plano_Capacitacao"(cod_plano_capacitacao),
    cod_prioridade_id integer references "Prioridade"(cod_prioridade),
    cod_treinamento_id integer references "Treinamento"(cod_treinamento),
    cod_turno_id integer references "Turno"(cod_turno)
);

CREATE TABLE "Avaliacao" (
    cod_avaliacao SERIAL PRIMARY KEY,
    valor_custo numeric(17,2) NOT NULL,
    ind_excluido numeric(2,0) NOT NULL,
    cod_necessidade_id integer references "Necessidade"(cod_necessidade)
);

CREATE TABLE "Secretaria" (
    cod_secretaria SERIAL PRIMARY KEY,
    nome character varying(200) NOT NULL
);

CREATE TABLE "Permissao" (
    cod_permissao SERIAL PRIMARY KEY,
    ano_plano_capacitacao numeric(4,0) NOT NULL,
    cod_secretaria_id integer references "Secretaria"(cod_secretaria),
    cod_tipo_plano_capacitacao_id integer references "Tipo_Plano_Capacitacao"(cod_tipo_plano_capacitacao)
);






-- CREATE TABLE auth_group (
--     id SERIAL PRIMARY KEY,
--     name character varying(80) NOT NULL
-- );

-- CREATE TABLE auth_group_permissions (
--     id SERIAL PRIMARY KEY,
--     group_id integer NOT NULL,
--     permission_id integer NOT NULL
-- );

-- CREATE TABLE auth_permission (
--     id SERIAL PRIMARY KEY,
--     name character varying(255) NOT NULL,
--     content_type_id integer NOT NULL,
--     codename character varying(100) NOT NULL
-- );


-- CREATE TABLE auth_user (
--     id SERIAL PRIMARY KEY,
--     password character varying(128),
--     last_login timestamp with time zone,
--     is_superuser boolean NOT NULL,
--     username character varying(150) NOT NULL,
--     first_name character varying(50) NOT NULL,
--     last_name character varying(150) NOT NULL,
--     email character varying(254),
--     is_staff boolean NOT NULL,
--     is_active boolean NOT NULL,
--     date_joined timestamp with time zone
-- );

-- CREATE TABLE auth_user_groups (
--     id SERIAL PRIMARY KEY,
--     user_id integer NOT NULL,
--     group_id integer NOT NULL
-- );

-- CREATE TABLE auth_user_user_permissions (
--     id SERIAL PRIMARY KEY,
--     user_id integer NOT NULL,
--     permission_id integer NOT NULL
-- );

CREATE TABLE capacita_profile (
    id SERIAL PRIMARY KEY,
    titular boolean,
    permissao_necessidade boolean,
    orgao_id integer,
    user_id integer NOT NULL
);

-- CREATE TABLE django_admin_log (
--     id SERIAL PRIMARY KEY,
--     action_time timestamp with time zone NOT NULL,
--     object_id text,
--     object_repr character varying(200) NOT NULL,
--     action_flag smallint NOT NULL,
--     change_message text NOT NULL,
--     content_type_id integer,
--     user_id integer NOT NULL,
--     CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
-- );


-- CREATE TABLE django_cas_ng_proxygrantingticket (
--     id SERIAL PRIMARY KEYL,
--     session_key character varying(255),
--     pgtiou character varying(255),
--     pgt character varying(255),
--     date timestamp with time zone NOT NULL,
--     user_id integer
-- );

-- CREATE TABLE django_cas_ng_sessionticket (
--     id SERIAL PRIMARY KEY,
--     session_key character varying(255) NOT NULL,
--     ticket character varying(255) NOT NULL
-- );


-- CREATE TABLE django_content_type (
--     id SERIAL PRIMARY KEY,
--     app_label character varying(100) NOT NULL,
--     model character varying(100) NOT NULL
-- );

-- CREATE TABLE django_migrations (
--     id SERIAL PRIMARY KEY,
--     app character varying(255) NOT NULL,
--     name character varying(255) NOT NULL,
--     applied timestamp with time zone NOT NULL
-- );

-- CREATE TABLE django_session (
--     session_key character varying(40) PRIMARY KEY,
--     session_data text NOT NULL,
--     expire_date timestamp with time zone NOT NULL
-- );

insert into "Objetivo_Treinamento" (cod_objetivo_treinamento, nome) values (0,'Atendimento ao usuário da área');
insert into "Objetivo_Treinamento" (cod_objetivo_treinamento, nome) values (1,'Aperfeiçoamento das atividades da área');


insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (266,'Comunicaçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (292,'Ciencia da Computaçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (294,'Direito', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (295,'Administraçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (296,'Economia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (297,'Demografia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (299,'Ciencia da Informaçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (300,'Serviço Social', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (301,'Sociologia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (302,'Antropologia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (303,'Arqueologia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (304,'Geografia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (305,'Ciencia Politica', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (306,'Matematica', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (307,'Probabilidade e Estatistica', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (308,'Ciencias Biologicas', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (309,'Engenharias', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (310,'Ciencias da Saude', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (311,'Arquitetura', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (312,'Ciencia da Informaçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (313,'Ciencias Humanas', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (314,'Psicologia', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (315,'Educaçao', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (316,'Letras', 0);
insert into "Area_Conhecimento" (cod_area_conhecimento, txt_descricao, ind_excluido) values (-1,'Outro', 0);

insert into "Iniciativa" (cod_iniciativa, nome) values (1, 'Senado');

insert into "Mes" values (1,'Janeiro');
insert into "Mes" values (2,'Fevereiro');
insert into "Mes" values (3,'Março');
insert into "Mes" values (4,'Abril');
insert into "Mes" values (5,'Maio');
insert into "Mes" values (6,'Junho');
insert into "Mes" values (7,'Julho');
insert into "Mes" values (8,'Agosto');
insert into "Mes" values (9,'Setembro');
insert into "Mes" values (10,'Outubro');
insert into "Mes" values (11,'Novembro');
insert into "Mes" values (12,'Dezembro');

insert into "Evento" values (1,'Teste', 0);

insert into "Plano_Capacitacao" values (1, 10, 10, '09/05/2010', '09/05/2010', 2010, 0, FALSE);
insert into "Plano_Capacitacao" values (2, 10, 10, '09/05/2010', '09/05/2010', 2010, 0, TRUE);

INSERT INTO "public"."Necessidade" (cod_necessidade,txt_descricao,qtd_servidor,hor_duracao,ind_excluido,custo,aprovado,justificativa,cod_area_conhecimento_id,cod_evento_id,cod_modalidade_id,cod_nivel_id,cod_plano_capacitacao_id,cod_prioridade_id,cod_tipo_id,cod_usuario_id,treinamento_id) VALUES (1,'s',1 , 1, 1, 1, FALSE, 's', 266, 1, 1, 1, 1, 1, 1, 1, 1);

insert into "Nivel" (cod_nivel, nome) values (1,'facil');
insert into "Nivel" (cod_nivel, nome) values (2,'medio');
insert into "Nivel" (cod_nivel, nome) values (3,'dificil');

insert into "Orgao" (cod_orgao, nome) values (3,'COARQ');
insert into "Orgao" (cod_orgao, nome) values (4,'COPOPE');
insert into "Orgao" (cod_orgao, nome) values (5,'COATREL');
insert into "Orgao" (cod_orgao, nome) values (6,'COPAG');
insert into "Orgao" (cod_orgao, nome) values (7,'COCETI');
insert into "Orgao" (cod_orgao, nome) values (8,'COEMAT');
insert into "Orgao" (cod_orgao, nome) values (9,'COGENV');
insert into "Orgao" (cod_orgao, nome) values (10,'COGEFI');
insert into "Orgao" (cod_orgao, nome) values (11,'COREM');
insert into "Orgao" (cod_orgao, nome) values (12,'COEDIT');
insert into "Orgao" (cod_orgao, nome) values (13,'ATEC');
insert into "Orgao" (cod_orgao, nome) values (14,'ATDGER');
insert into "Orgao" (cod_orgao, nome) values (15,'COOTELE');
insert into "Orgao" (cod_orgao, nome) values (16,'COIND');
insert into "Orgao" (cod_orgao, nome) values (17,'COASAS');
insert into "Orgao" (cod_orgao, nome) values (18,'COAPAT');
insert into "Orgao" (cod_orgao, nome) values (19,'COPROT');
insert into "Orgao" (cod_orgao, nome) values (20,'CORTEL');
insert into "Orgao" (cod_orgao, nome) values (21,'COAUDTI');
insert into "Orgao" (cod_orgao, nome) values (22,'COGER');
insert into "Orgao" (cod_orgao, nome) values (23,'COSUP');
insert into "Orgao" (cod_orgao, nome) values (24,'COPINV');
insert into "Orgao" (cod_orgao, nome) values (25,'CORTV');
insert into "Orgao" (cod_orgao, nome) values (26,'COADTV');
insert into "Orgao" (cod_orgao, nome) values (27,'COBEP');
insert into "Orgao" (cod_orgao, nome) values (28,'CORCOM');
insert into "Orgao" (cod_orgao, nome) values (29,'COAME');
insert into "Orgao" (cod_orgao, nome) values (30,'COASAL');
insert into "Orgao" (cod_orgao, nome) values (31,'CORER');
insert into "Orgao" (cod_orgao, nome) values (32,'COCDIR');
insert into "Orgao" (cod_orgao, nome) values (33,'COPAC');
insert into "Orgao" (cod_orgao, nome) values (34,'COPLAC');
insert into "Orgao" (cod_orgao, nome) values (35,'COGEP');
insert into "Orgao" (cod_orgao, nome) values (36,'CORDIACN');
insert into "Orgao" (cod_orgao, nome) values (37,'COTI');
insert into "Orgao" (cod_orgao, nome) values (38,'DATASEN');
insert into "Orgao" (cod_orgao, nome) values (39,'CONTV');
insert into "Orgao" (cod_orgao, nome) values (40,'COTIN');
insert into "Orgao" (cod_orgao, nome) values (41,'COMAP');
insert into "Orgao" (cod_orgao, nome) values (42,'COVISITA');
insert into "Orgao" (cod_orgao, nome) values (43,'COJORN');
insert into "Orgao" (cod_orgao, nome) values (44,'COEDAJS');
insert into "Orgao" (cod_orgao, nome) values (45,'COSTIC');
insert into "Orgao" (cod_orgao, nome) values (46,'COAUDGEP');
insert into "Orgao" (cod_orgao, nome) values (47,'COESUP');
insert into "Orgao" (cod_orgao, nome) values (48,'COADFI');
insert into "Orgao" (cod_orgao, nome) values (49,'COBERT');
insert into "Orgao" (cod_orgao, nome) values (50,'COPRTV');
insert into "Orgao" (cod_orgao, nome) values (51,'CONTAB');
insert into "Orgao" (cod_orgao, nome) values (52,'COINTI');
insert into "Orgao" (cod_orgao, nome) values (53,'COER');
insert into "Orgao" (cod_orgao, nome) values (54,'COVESP');
insert into "Orgao" (cod_orgao, nome) values (55,'COAUDCF');
insert into "Orgao" (cod_orgao, nome) values (56,'CODM');
insert into "Orgao" (cod_orgao, nome) values (57,'COPROJ');
insert into "Orgao" (cod_orgao, nome) values (58,'COELDI');
insert into "Orgao" (cod_orgao, nome) values (59,'COLEP');
insert into "Orgao" (cod_orgao, nome) values (60,'CORPLEN');
insert into "Orgao" (cod_orgao, nome) values (61,'COEXEFI');
insert into "Orgao" (cod_orgao, nome) values (62,'COEXPO');
insert into "Orgao" (cod_orgao, nome) values (63,'COORD');
insert into "Orgao" (cod_orgao, nome) values (64,'COBIB');
insert into "Orgao" (cod_orgao, nome) values (65,'COAPOP');
insert into "Orgao" (cod_orgao, nome) values (66,'COENGTVR');
insert into "Orgao" (cod_orgao, nome) values (67,'COPRE');
insert into "Orgao" (cod_orgao, nome) values (68,'COEXECO');
insert into "Orgao" (cod_orgao, nome) values (69,'COATC');
insert into "Orgao" (cod_orgao, nome) values (70,'COEMANT');
insert into "Orgao" (cod_orgao, nome) values (71,'COCPSF');
insert into "Orgao" (cod_orgao, nome) values (72,'COATEN');
insert into "Orgao" (cod_orgao, nome) values (73,'COPIL');
insert into "Orgao" (cod_orgao, nome) values (74,'COCM');
insert into "Orgao" (cod_orgao, nome) values (75,'CORED');
insert into "Orgao" (cod_orgao, nome) values (76,'COAPOT');
insert into "Orgao" (cod_orgao, nome) values (77,'CORELE');
insert into "Orgao" (cod_orgao, nome) values (78,'COAUDCON');
insert into "Orgao" (cod_orgao, nome) values (79,'EGOV');
insert into "Orgao" (cod_orgao, nome) values (80,'COASIS');
insert into "Orgao" (cod_orgao, nome) values (81,'COARO');
insert into "Orgao" (cod_orgao, nome) values (82,'COLECN');
insert into "Orgao" (cod_orgao, nome) values (83,'COAPES');
insert into "Orgao" (cod_orgao, nome) values (84,'COINTEL');
insert into "Orgao" (cod_orgao, nome) values (85,'ASSETEC');
insert into "Orgao" (cod_orgao, nome) values (86,'COAPEC');
insert into "Orgao" (cod_orgao, nome) values (87,'COALSGM');
insert into "Orgao" (cod_orgao, nome) values (88,'COMIL');
insert into "Orgao" (cod_orgao, nome) values (89,'COCVAP');
insert into "Orgao" (cod_orgao, nome) values (90,'COTREN');

insert into "Prioridade" (cod_prioridade, nome) values (1,'Baixa');
insert into "Prioridade" (cod_prioridade, nome) values (2,'Média');
insert into "Prioridade" (cod_prioridade, nome) values (3,'Alta');

insert into "Tipo_Plano_Capacitacao" (cod_tipo_plano_capacitacao, sgl_tipo_plano_capacitacao, nome_tipo_plano_capacitacao, ind_excluido) values (5,'CP','Corem Iosum', 0);

insert into "Turno" (cod_turno, nome) values (1,'Matutino');
insert into "Turno" (cod_turno, nome) values (2,'Vespertino');

insert into auth_group (id, name) values (1, 'admin');
insert into auth_group (id, name) values (2, 'gestor');
insert into auth_group (id, name) values (3, 'solicitante');

-- insert into auth_group_permissions (group_id, permission_id) values (1,1);
-- insert into auth_group_permissions (group_id, permission_id) values (1,2);
-- insert into auth_group_permissions (group_id, permission_id) values (1,3);
-- insert into auth_group_permissions (group_id, permission_id) values (1,4);
-- insert into auth_group_permissions (group_id, permission_id) values (1,5);
-- insert into auth_group_permissions (group_id, permission_id) values (1,6);
-- insert into auth_group_permissions (group_id, permission_id) values (1,7);
-- insert into auth_group_permissions (group_id, permission_id) values (1,8);
-- insert into auth_group_permissions (group_id, permission_id) values (1,9);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,10);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,11);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,12);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,13);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,14);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,15);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,16);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,17);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,18);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,19);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,20);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,21);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,22);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,23);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,24);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,25);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,26);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,27);
-- insert into auth_group_permissions (group_id, permission_id) values (1,28);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,29);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,30);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,31);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,32);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,33);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,34);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,35);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,36);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,37);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,38);
-- insert into auth_group_permissions (group_id, permission_id) values (1,39);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,40);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,41);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,42);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,43);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,44);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,45);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,46);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,47);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,48);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,49);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,50);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,51);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,52);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,53);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,54);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,55);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,56);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,57);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,58);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,59);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,60);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,61);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,62);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,63);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,64);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,65);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,66);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,67);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,68);
-- insert into auth_group_permissions (group_id, permission_id) values ( 1,69);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,1);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,2);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,4);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,5);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,7);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,8);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,10);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,11);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,13);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,14);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,22);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,23);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,25);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,26);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,28);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,29);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,31);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,32);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,34);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,35);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,37);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,38);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,40);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,41);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,43);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,44);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,46);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,47);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,49);
-- insert into auth_group_permissions (group_id, permission_id) values ( 2,50);
-- insert into auth_group_permissions (group_id, permission_id) values (2,52);
-- insert into auth_group_permissions (group_id, permission_id) values (2,53);
-- insert into auth_group_permissions (group_id, permission_id) values (2,55);
-- insert into auth_group_permissions (group_id, permission_id) values (2,56);
-- insert into auth_group_permissions (group_id, permission_id) values (2,58);
-- insert into auth_group_permissions (group_id, permission_id) values (2,59);
-- insert into auth_group_permissions (group_id, permission_id) values (2,61);
-- insert into auth_group_permissions (group_id, permission_id) values (2,62);
-- insert into auth_group_permissions (group_id, permission_id) values (2,64);
-- insert into auth_group_permissions (group_id, permission_id) values (2,65);
-- insert into auth_group_permissions (group_id, permission_id) values (2,67);
-- insert into auth_group_permissions (group_id, permission_id) values (2,68);
-- insert into auth_group_permissions (group_id, permission_id) values (3,1);
-- insert into auth_group_permissions (group_id, permission_id) values (3,2);
-- insert into auth_group_permissions (group_id, permission_id) values (3,19);
-- insert into auth_group_permissions (group_id, permission_id) values (3,52);
-- insert into auth_group_permissions (group_id, permission_id) values (3,20);
-- insert into auth_group_permissions (group_id, permission_id) values (3,22);
-- insert into auth_group_permissions (group_id, permission_id) values (3,23);

-- insert into auth_permission ( name, content_type_id, codename) values ('Can add log entry', 1, 'add_logentry');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can change log entry', 1, 'change_logentry');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can delete log entry', 1, 'delete_logentry');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can add user',2, 'add_user');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can change user',2, 'change_user');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can delete user',2, 'delete_user');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can add group', 3, 'add_group');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can change group' ,3, 'change_group');
-- insert into auth_permission ( name, content_type_id, codename) values ('Can delete group', 3, 'delete_group');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add permission', 4, 'add_permission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change permission',4, 'change_permission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete permission',4, 'delete_permission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add content type', 5, 'add_contenttype');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change content type',5, 'change_contenttype');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete content type', 5, 'delete_contenttype');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add session', 6, 'add_session');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change session', 6 ,'change_session');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete session', 6,'delete_session');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add session ticket', 7,'add_sessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change session ticket', 7,'change_sessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete session ticket', 7,'delete_sessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add proxy granting ticket', 8,'add_proxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change proxy granting ticket',8,'change_proxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete proxy granting ticket',8,'delete_proxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add turno', 9,'add_turno');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change turno', 9,'change_turno');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete turno', 9,'delete_turno');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add permissao', 10,  'add_permissao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change permissao', 10,  'change_permissao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete permissao', 10,  'delete_permissao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add area_ conhecimento',  11,  'add_area_conhecimento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change area_ conhecimento', 11,  'change_area_conhecimento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete area_ conhecimento', 11,  'delete_area_conhecimento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add profile' ,12,  'add_profile');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change profile',  12,  'change_profile');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete profile',  12,  'delete_profile');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add mes', 13,  'add_mes');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change mes',  13,  'change_mes');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete mes',  13,  'delete_mes');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add plano_ capacitacao', 14, 'add_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change plano_ capacitacao', 14, 'change_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete plano_ capacitacao', 14, 'delete_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add avaliacao', 15,  'add_avaliacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change avaliacao', 15,  'change_avaliacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete avaliacao', 15,  'delete_avaliacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add iniciativa', 16,  'add_iniciativa');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change iniciativa', 16,  'change_iniciativa');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete iniciativa', 16 , 'delete_iniciativa');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add orgao', 17 , 'add_orgao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change orgao', 17 , 'change_orgao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete orgao', 17  ,'delete_orgao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add necessidade', 18,  'add_necessidade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change necessidade', 18,  'change_necessidade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete necessidade', 18,  'delete_necessidade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add nivel', 19,  'add_nivel');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change nivel', 19,  'change_nivel');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete nivel', 19,  'delete_nivel');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add secretaria', 20,  'add_secretaria');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change secretaria', 20,  'change_secretaria');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete secretaria', 20,  'delete_secretaria');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add sub_ area_ conhecimento' ,21,  'add_treinamento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change sub_ area_ conhecimento', 21,  'change_treinamento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete sub_ area_ conhecimento', 21,'delete_treinamento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add tipo_ plano_ capacitacao',22,  'add_tipo_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change tipo_ plano_ capacitacao' ,22,  'change_tipo_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete tipo_ plano_ capacitacao' ,22 , 'delete_tipo_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add prioridade',23,  'add_prioridade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change prioridade',23,  'change_prioridade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete prioridade',23,  'delete_prioridade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view log entry', 1,'view_logentry');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view permission', 4,'view_permission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view user', 2,'view_user');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view group', 3,'view_group');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view content type', 5,'view_contenttype');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view session', 6,'view_session');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view proxy granting ticket',  8,'view_proxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view session ticket', 7,'view_sessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view iniciativa', 16,'view_iniciativa');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view profile', 12,  'view_profile');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view mes', 13,  'view_mes');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view necessidade', 18,  'view_necessidade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view permissao', 10 ,  'view_permissao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view prioridade', 23, 'view_prioridade');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view secretaria', 20,  'view_secretaria');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view orgao',  17,  'view_orgao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view turno',  9,'view_turno');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view plano_ capacitacao', 14,  'view_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view tipo_ plano_ capacitacao',22,  'view_tipo_plano_capacitacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view avaliacao', 15,  'view_avaliacao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view sub_ area_ conhecimento', 21,  'view_treinamento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view area_ conhecimento', 11,  'view_area_conhecimento');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view nivel',19,' view_nivel');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add acao',  24, 'add_acao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change acao', 24, 'change_acao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete acao', 24, 'delete_acao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view acao', 24, 'view_acao');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add django admin log', 25, 'add_djangoadminlog');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change django admin log', 25, 'change_djangoadminlog');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete django admin log', 25, 'delete_djangoadminlog');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view django admin log', 25, 'view_djangoadminlog');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add auth permission', 26, 'add_authpermission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change auth permission', 26, 'change_authpermission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete auth permission', 26, 'delete_authpermission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can view auth permission', 26 , 'view_authpermission');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can add auth user',27,  'add_authuser');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can change auth user', 27,  'change_authuser');
-- insert into auth_permission ( name, content_type_id, codename) values  ('Can delete auth user', 27,  'delete_authuser');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view auth user',  27,  'view_authuser');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add django cas ng sessionticket', 28,  'add_djangocasngsessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change django cas ng sessionticket',  28,  'change_djangocasngsessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete django cas ng sessionticket',  28,  'delete_djangocasngsessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view django cas ng sessionticket', 28,  'view_djangocasngsessionticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add auth group',  29,  'add_authgroup');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change auth group', 29,  'change_authgroup');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete auth group', 29,  'delete_authgroup');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view auth group', 29,  'view_authgroup');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add auth user user permissions',  30,  'add_authuseruserpermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change auth user user permissions', 30,  'change_authuseruserpermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete auth user user permissions', 30,  'delete_authuseruserpermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view auth user user permissions', 30,  'view_authuseruserpermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add auth user groups', 31, 'add_authusergroups');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change auth user groups', 31,  'change_authusergroups');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete auth user groups', 31,  'delete_authusergroups');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view auth user groups', 31,  'view_authusergroups');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add django migrations', 32,  'add_djangomigrations');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change django migrations', 32,  'change_djangomigrations');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete django migrations', 32,  'delete_djangomigrations');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view django migrations', 32,  'view_djangomigrations');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add auth group permissions',33,  'add_authgrouppermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change auth group permissions', 33,  'change_authgrouppermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete auth group permissions', 33,  'delete_authgrouppermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view auth group permissions',33,'view_authgrouppermissions');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add django cas ng proxygrantingticket', 34,  'add_djangocasngproxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change django cas ng proxygrantingticket', 34,  'change_djangocasngproxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete django cas ng proxygrantingticket', 34,  'delete_djangocasngproxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view django cas ng proxygrantingticket',34,  'view_djangocasngproxygrantingticket');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add django session', 35, 'add_djangosession');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change django session', 35,  'change_djangosession');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete django session', 35,  'delete_djangosession');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view django session', 35, 'view_djangosession');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can add django content type', 36,  'add_djangocontenttype');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can change django content type', 36,  'change_djangocontenttype');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can delete django content type',  36,  'delete_djangocontenttype');
-- insert into auth_permission ( name, content_type_id, codename) values ( 'Can view django content type', 36,  'view_djangocontenttype');


insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (48 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'rrgrosse', 'ROBERTO', 'RICARDO CARLOS GROSSE JÚNIOR' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (49 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'fsebben', 'FERNANDO', 'DALL ONDER SEBBEN'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (50 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'geovanes', 'GEOVANE', 'RESENDE SILVA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (51 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'tiagofff', 'TIAGO',   'FERNANDES FELIX DE FARIA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (52 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'brunols', 'EDUARDO', 'BRUNO DO LAGO DE SA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (53 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'rfmoraes', 'RICARDO', 'FREITAS DE MORAES'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (54 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'herivel', 'HERIVELTO' ,'FERREIRA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (55 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'pabloc', 'PABLO',   'DIEGO BARROS DA CONCEIÇÃO'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (56 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'mmuniz' , 'MARCELO', 'MUNIZ DE MELO'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (57 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'abvi', 'ALOYSIO', 'DE BRITO VIEIRA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (58 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'wgto', 'WASHINGTON',  'MANOEL BRITO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (59 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'baldutti', 'EVANDRO', 'APARECIDO BALDUTTI'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (60 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'orlandoc', 'ORLANDO', 'CARNEIRO SILVA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (61 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'hezevedo', 'HÉLIO',  'LOPES DE AZEVEDO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (62 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'kairalak', 'KAIRALA', 'JOSÉ KAIRALA FILHO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (63 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'cleberaz', 'CLEBER',  'DE AZEVEDO SILVA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (64 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'claudhil', 'CLÁUDIO', 'HILÁRIO DE SOUZA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (65 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'deraldor', 'DERALDO', 'RUAS GUIMARÃES'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (66 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'celopes', 'CARLOS',  'EDUARDO LOPES NEVES'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (67 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'lara', 'ROBERTO', 'LARA DA ROCHA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (68 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'afgomes', 'ADRIANO', 'FERNANDES GOMES'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (69 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'evbosco', 'EVERALDO', 'BOSCO ROSA MOREIRA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (70 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'barizon', 'JOÃO', 'CARLOS BARIZON'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (71 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'clayto',  'CLAYTON', 'FERREIRA DE LIRA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (72 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'lneide',  'LUCINEIDE',   'SOARES DA SILVA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (73 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'valesca', 'VALESCA', 'NEIVA MARTINS'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (74 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'paton',   'PATRÍCIA', 'DE OLIVEIRA NÓBREGA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (75 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'nobreces', 'ANTÔNIO', 'CÉSAR NOBREGA DE MOURA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (76 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'fabiocm', 'FABIO',   'COSTA MELO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (77 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'mabeme',  'MARCOS',  'ANDRÉ BEZERRA MESQUITA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (78 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'maxper',  'MAXWELL', 'PERONA RIBEIRO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (79 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'amattos', 'ALEXANDRE',   'MATTOS DE FREITAS'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (80 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'said', 'ANDRÉ','SAID DE LAVOR'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (81 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'edimarf', 'EDIMAR',  'LUIZ DA SILVA FILHO'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (82 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'glebson', 'GLEBSON', 'MOURA DA SILVA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (83 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'faacm',   'FLORIAN', 'AUGUSTO DE ABREU COUTINHO MADRUGA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (84 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'ronaldom', 'RONALDO' ,'PEREIRA MARTINS'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (85 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'sevieira', 'SESOSTRIS',   'VIEIRA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (86 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'fabioad', 'FÁBIO',   'ALVES DUARTE' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (87 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'marimt',  'MARIANA', 'MIRANDA TAVARES'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (88 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,    'marciomc', 'MARCIO',  'MATURANA CARDOSO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (3  , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'brunocordeiro180', 'BRUNO', 'CORDEIRO', FALSE, TRUE);
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (4  , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com' ,FALSE,   'lulinha', 'LUIZ', 'INÁCIO LULA da SILVA', FALSE, TRUE);
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (5  , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com' ,FALSE,   'ciro', 'CIRO', 'GOMES', FALSE, TRUE);
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (89 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'andrefrb', 'ANDRE',   'FALCAO DO REGO BARROS'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (90 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'gleisong', 'GLEISON', 'CARNEIRO GOMES'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (91 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'joaovrp', 'JOÃO', 'VICENTE DA ROCHA PESSOA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (92 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'lela', 'VALÉRIA', 'RIBEIRO DA SILVA FRANKLIN ALMEIDA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (93 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'claudioa', 'CLÁUDIO', 'ALVES CAVALCANTE' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (94 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'paolamic', 'PAOLA',   'MICHELLE NOGUEIRA DE CERQUEIRA LIMA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (95 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'tiagomcn', 'TIAGO',   'MACINI'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (96 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'lhpaiva', 'LUIZ', 'HENRIQUE DE PAIVA MARQUES'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (97 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'molina',  'ANDRE',   'LUIZ BANDEIRA MOLINA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (98 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'joaom',   'JOÃO', 'MARCOS MURCE MENESES' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (99 , '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'amandara','AMANDA',  'RODRIGUES DE ALBUQUERQUE' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (100, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'sergiop', 'SERGIO',  'GERONIMO PEREIRA BONIFACIO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (101, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'danielps',    'DANIEL'  ,'PEREIRA SANTANA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (102, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'kalink', 'KALINKA', 'DE SÁ HOLANDA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (103, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'fabianor',    'FABIANO', 'SANTOS REZENDE DE ARAUJO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (104, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'patgomes',    'PATRICIA',   'GOMES DE CARVALHO CARNEIRO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (105, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'vladner', 'VLADNER', 'LIMA BARROS LEAL' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (106, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'patriab', 'PATRÍCIA',    'DE ANDRADE BENTES'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (107, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'leorgf',  'LEONARDO',    'DOS REIS GUEDES FERREIRA' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (108, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'isamaria',    'ISA', 'MARIA   DE CASTRO DIAS MAGALHÃES' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (109, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'marcoscd',    'MARCOS',  'HELDER CRISÓSTOMO DAMASCENO'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (110, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'morizzo', 'MÔNICA',  'ALMEIDA RIZZO SOARES' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (111, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'raphaelc',    'RAPHAEL', 'SALGADO CARDOSO SILVA'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (112, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'joverlan', 'JOVERLANDIO', 'NUNES DE SOUZA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (113, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'ronienc', 'RONILDO', 'PIRES DE ALMEIDA JÚNIOR'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (114, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'alexper', 'ALEXANDRE','CARDOSO PEREIRA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (115, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'allan',   'ALLAN', 'DEL CISTIA MELLO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (116, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'laurojnr','LAURO',   'ALVES DE OLIVEIRA JÚNIOR' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (117, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'brunocl', 'BRUNO',   'CUNHA LIMA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (118, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'hcortez', 'HEITOR',  'OLIVEIRA CORTEZ'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (119, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'dslabes', 'DENIS',  'SILVA LABES'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (120, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'mmmelo',  'MARCOS',  'MACHADO MELO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (121, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'fnardelli',   'FERNANDA', 'NARDELLI DE CARVALHO CARDIM'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (122, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'airesjr', 'AIRES','PEREIRA DAS NEVES JUNIOR' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (123, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'catelli', 'MARCELO', 'PICOLO CATELLI'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (124, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'diogomn', 'DIOGO', 'MACEDO DE NOVAES' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (125, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'gaborges',    'GABRIELA', 'AGUSTINHO BORGES'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (126, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'ramonms', 'RAMON', 'MENDES DE SOUZA'  ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (127, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'seabreno',    'BRENO',   'DA SILVA BRANDÃO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (128, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'muniqueb',    'MUNIQUE', 'BARROS DE CARVALHO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (129, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'matheusc',    'MATHEUS', 'MEDEIROS MACHADO CARRION DE MACEDO'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (130, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'sabrina', 'SABRINA', 'SILVA NASCIMENTO' ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (131, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'gilver',  'GILVERLAN',   'PESSOA PEREIRA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (132, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'alissonb', 'ALISSON', 'BRUNO DIAS DE QUEIROZ'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (133, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'cassios', 'CÁSSIO',  'DOS SANTOS ARAUJO'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (134, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'erikamb', 'ERIKA',   'MARA BARBACENA'   ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (135, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,FALSE,   'pandini', 'EMERSON', 'JADER PANDINI'    ,FALSE   ,TRUE   );
insert into auth_user (id, password, date_joined, email, is_superuser, username, first_name, last_name, is_staff, is_active) values (138, '0', '2018-09-11 15:16:45-03', 'teste@gmail.com'  ,TRUE,   'brunocm', 'Bruno', 'Cordeiro', TRUE   ,TRUE  );

insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (234,  'Distribuição Espacial',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (235,  'Tendência Populacional',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (236,  'Componentes da Dinâmica Demográfica',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (237,  'Nupcialidade e Família',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (238,  'Demografia Histórica',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (239,  'Política Pública e População',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (240,  'Fontes de Dados Demográficos',297);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (258,  'Teoria da Informaçao',299);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (259,  'Biblioteconomia',299);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (260,  'Arquivologia',299);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (261,  'Fundamentos do Serviço Social',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (263,  'Fundamentos da Sociologia',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (264,  'Sociologia do Conhecimento',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (265,  'Sociologia do Desenvolvimento',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (266,  'Sociologia Urbana',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (267,  'Sociologia Rural',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (268,  'Sociologia da Saude',301);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (269,  'Teoria Antropologica',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (270,  'Etnologia Indigena',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (271,  'Antropologia Urbana',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (272,  'Antropologia Rural',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (273,  'Sociologia Rural',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (274,  'Antropologia das Populações Afro-Brasileiras',302);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (275,  'Teoria e Método em Arqueologia',303);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (276,  'Arqueologia Pré-Histórica',303);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (277,  'Arqueologia Histórica',303);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (278,  'Geografia Humana',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (279,  'Geografia Regional',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (280,  'Teoria Politica',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (281,  'Estado e Governo',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (282,  'Comportamento Politico',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (283,  'Politicas Publicas',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (284,  'Politica Internacional',304);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (285,  'Algebra',306);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (286,  'Analise',306);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (287,  'Geometria e Topologia',306);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (288,  'Matematica Aplicada',306);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (289,  'Probabilidade',307);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (290,  'Estatistica',307);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (291,  'Probabilidade e Estatistica Aplicada',307);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (292,  'Computabilidade e Modelos de Computação',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (293,  'Linguagem Formais e Automatos',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (294,  'Análise de Algoritmos e Complexidade de Computação',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (295,  'Lógicas e Semântica de Programas',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (296,  'Matemática Simbólica',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (297,  'Modelos Analíticos e de Simulação',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (298,  'Linguagens de Programação',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (299,  'Engenharia de Software',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (300,  'Banco de Dados',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (301,  'Sistemas de Informaçãos',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (302,  'Banco de Dados',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (303,  'Processamento Gráfico (Graphics)',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (304,  'Hardware',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (305,  'Arquitetura de Sistemas de Computação',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (306,  'Software Básico',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (307,  'Teleinformática',292);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (308,  'Biologia Geral',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (309,  'Genética',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (310,  'Botânica',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (311,  'Zoologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (312,  'Ecologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (313,  'Morfologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (314,  'Fisiologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (315,  'Bioquímica',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (316,  'Biofísica',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (317,  'Farmacologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (318,  'Imunologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (319,  'Microbiologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (320,  'Parasitologia',308);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (321,  'Engenharia Civil',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (322,  'Engenharia de Minas',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (323,  'Engenharia de Materiais e Metalúrgica',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (324,  'Engenharia Elétrica',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (325,  'Engenharia Mecânica',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (326,  'Engenharia Química',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (327,  'Engenharia Sanitária',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (328,  'Engenharia de Produção',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (329,  'Engenharia Nuclear',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (330,  'Engenharia de Transportes',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (331,  'Engenharia Biomédica',309);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (332,  'Medicina',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (333,  'Odontologia',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (334,  'Farmacia',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (335,  'Enfermagem',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (336,  'Nutriçao',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (337,  'Saude Coletiva',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (338,  'Fonoaudiologia',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (339,  'Fisioterapia e Terapia Ocupacional',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (340,  'Educação Física',310);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (341,  'Teoria Geral do Direito',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (342,  'Teoria Geral do Processo',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (343,  'Teoria do Estado',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (344,  'História do Direito',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (345,  'Filosofia do Direito',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (346,  'Lógica Jurídica',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (347,  'Sociologia Jurídica',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (348,  'Antropologia Jurídica',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (349,  'Direito Tributário',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (350,  'Direito Penal',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (351,  'Direito Processual Penal',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (352,  'Direito Processual Civil',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (353,  'Direito Constitucional',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (354,  'Direito Administrativo',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (355,  'Direito Internacional Público',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (356,  'Direito Civil',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (357,  'Direito Comercial',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (358,  'Direito do Trabalho',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (359,  'Direito Internacional Privado',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (360,  'Direitos Especiais',294);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (361,  'Administração da Produção',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (362,  'Administração Financeira',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (363,  'Mercadologia',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (364,  'Negócios Internacionais',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (365,  'Administração de Recursos Humanos',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (366,  'Contabilidade e Financas Públicas',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (367,  'Organizações Públicas',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (368,  'Política e Planejamento Governamentais',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (369,  'Administração de Pessoal',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (370,  'Administração de Setores Específicos',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (371,  'Ciências Contábeis',295);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (372,  'Economia Geral',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (373,  'Teoria Geral da Economia',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (374,  'História do Pensamento Econômico',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (375,  'História Econômica',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (376,  'Sistemas Econômicos',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (377,  'Métodos e Modelos Matemáticos, Econométricos e Estatísticos',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (378,  'Estatística Sócio-Econômica',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (379,  'Contabilidade Nacional',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (380,  'Economia Matemática',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (381,  'Teoria Monetária e Financeira',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (382,  'Instituições Monetárias e Financeiras do Brasil',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (383,  'Financas Públicas Internas',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (384,  'Política Fiscal do Brasil',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (385,  'Crescimento e Desenvolvimento Econômico',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (386,  'Teoria e Política de Planejamento Econômico',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (387,  'Flutuações Cíclicas e Projeções Econômicas',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (388,  'Inflação',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (389,  'Teoria do Comércio Internacional',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (390,  'Relações do Comércio; Política Comercial; Integração Econômica',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (391,  'Balanço de Pagamentos; Financas Internacionais',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (392,  'Treinamento e Alocação de Mão-de-Obra; Oferta de Mão-de-Obra e Força de Trabalho',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (393,  'Mercado de Trabalho; Política do Governo',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (394,  'Sindicatos, Dissídios Coletivos, Relações de Emprego (Empregador/Empregado)',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (395,  'Capital Humano',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (396,  'Demografia Econômica',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (397,  'Organização Industrial e Estudos Industriais',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (398,  'Mudança Tecnologica',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (399,  'Economia dos Programas de Bem-Estar Socia',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (400,  'Economia do Consumidor',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (401,  'Economia Regional',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (402,  'Economia Urbana',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (403,  'Renda e Tributação',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (404,  'Economia Agrária',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (405,  'Economia dos Recursos Naturais',296);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (406,  'Fundamentos de Arquitetura e Urbanismo',311);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (407,  'Projeto de Arquitetuta e Urbanismo',311);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (408,  'Tecnologia de Arquitetura e Urbanismo',311);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (409,  'Paisagismo',311);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (410,  'Teoria Geral da Informação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (411,  'Processos da Comunicação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (412,  'Representação da Informação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (413,  'Teoria da Classificação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (414,  'Métodos Quantitativos. Bibliometria',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (415,  'Técnicas de Recuperação de Informação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (416,  'Processos de Disseminação da Informação',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (417,  'Organização de Arquivos',312);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (418,  'Teoria da Comunicação',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (419,  'Teoria e Ética do Jornalismo',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (420,  'Organização Editorial de Jornais',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (421,  'Organização Comercial de Jornais',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (422,  'Jornalismo Especializado (Comunitário, Rural, Empresarial, Científico)',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (423,  'Radiodifusão',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (424,  'Videodifusão',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (425,  'Relações Públicas e Propaganda',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (426,  'Comunicação Visual',266);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (427,  'Serviço Social do Trabalho',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (428,  'Serviço Social da Educação',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (429,  'Serviço Social do Menor',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (430,  'Serviço Social da Saúde',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (431,  'Serviço Social da Habitação',300);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (432,  'Filosofia',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (433,  'Sociologia',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (434,  'Antropologia',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (435,  'Arqueologia',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (436,  'História',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (437,  'Geografia',313);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (438,  'Fundamentos e Medidas da Psicologia',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (439,  'Psicologia Experimental',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (440,  'Psicologia Fisiológica',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (441,  'Psicologia Comparativa',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (442,  'Psicologia Social',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (443,  'Psicologia Cognitiva',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (444,  'Psicologia do Desenvolvimento Humano',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (445,  'Psicologia do Ensino e da Aprendizagem',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (446,  'Psicologia do Trabalho e Organizacional',314);
insert into "Treinamento" (cod_treinamento, nome, cod_area_conhecimento_id) values (-1,  'Outro',-1);


insert into auth_user_groups (id, user_id, group_id) values (1 , 3   ,1);
insert into auth_user_groups (id, user_id, group_id) values (3 , 5   ,3);
insert into auth_user_groups (id, user_id, group_id) values (5 , 49  ,2);
insert into auth_user_groups (id, user_id, group_id) values (6 , 50  ,2);
insert into auth_user_groups (id, user_id, group_id) values (7 , 51  ,2);
insert into auth_user_groups (id, user_id, group_id) values (8 , 52  ,2);
insert into auth_user_groups (id, user_id, group_id) values (9 , 53  ,2);
insert into auth_user_groups (id, user_id, group_id) values (10, 54  ,2);
insert into auth_user_groups (id, user_id, group_id) values (11, 55  ,2);
insert into auth_user_groups (id, user_id, group_id) values (12, 56  ,2);
insert into auth_user_groups (id, user_id, group_id) values (13, 57  ,2);
insert into auth_user_groups (id, user_id, group_id) values (14, 58  ,2);
insert into auth_user_groups (id, user_id, group_id) values (15, 59  ,2);
insert into auth_user_groups (id, user_id, group_id) values (16, 60  ,2);
insert into auth_user_groups (id, user_id, group_id) values (17, 61  ,2);
insert into auth_user_groups (id, user_id, group_id) values (18, 62  ,2);
insert into auth_user_groups (id, user_id, group_id) values (19, 63  ,2);
insert into auth_user_groups (id, user_id, group_id) values (20, 64  ,2);
insert into auth_user_groups (id, user_id, group_id) values (21, 65  ,2);
insert into auth_user_groups (id, user_id, group_id) values (22, 66  ,2);
insert into auth_user_groups (id, user_id, group_id) values (23, 67  ,2);
insert into auth_user_groups (id, user_id, group_id) values (24, 68  ,2);
insert into auth_user_groups (id, user_id, group_id) values (25, 69  ,2);
insert into auth_user_groups (id, user_id, group_id) values (26, 70  ,2);
insert into auth_user_groups (id, user_id, group_id) values (27, 71  ,2);
insert into auth_user_groups (id, user_id, group_id) values (28, 72  ,2);
insert into auth_user_groups (id, user_id, group_id) values (29, 73  ,2);
insert into auth_user_groups (id, user_id, group_id) values (30, 74  ,2);
insert into auth_user_groups (id, user_id, group_id) values (31, 75  ,2);
insert into auth_user_groups (id, user_id, group_id) values (32, 76  ,2);
insert into auth_user_groups (id, user_id, group_id) values (33, 77  ,2);
insert into auth_user_groups (id, user_id, group_id) values (34, 78  ,2);
insert into auth_user_groups (id, user_id, group_id) values (35, 79  ,2);
insert into auth_user_groups (id, user_id, group_id) values (36, 80  ,2);
insert into auth_user_groups (id, user_id, group_id) values (37, 81  ,2);
insert into auth_user_groups (id, user_id, group_id) values (38, 82  ,2);
insert into auth_user_groups (id, user_id, group_id) values (39, 83  ,2);
insert into auth_user_groups (id, user_id, group_id) values (40, 84  ,2);
insert into auth_user_groups (id, user_id, group_id) values (41, 85  ,2);
insert into auth_user_groups (id, user_id, group_id) values (42, 86  ,2);
insert into auth_user_groups (id, user_id, group_id) values (43, 87  ,2);
insert into auth_user_groups (id, user_id, group_id) values (44, 88  ,2);
insert into auth_user_groups (id, user_id, group_id) values (45, 89  ,2);
insert into auth_user_groups (id, user_id, group_id) values (46, 90  ,2);
insert into auth_user_groups (id, user_id, group_id) values (47, 91  ,2);
insert into auth_user_groups (id, user_id, group_id) values (48, 92  ,2);
insert into auth_user_groups (id, user_id, group_id) values (49, 93  ,2);
insert into auth_user_groups (id, user_id, group_id) values (50, 94  ,2);
insert into auth_user_groups (id, user_id, group_id) values (51, 95  ,2);
insert into auth_user_groups (id, user_id, group_id) values (52, 96  ,2);
insert into auth_user_groups (id, user_id, group_id) values (53, 97  ,2);
insert into auth_user_groups (id, user_id, group_id) values (54, 98  ,2);
insert into auth_user_groups (id, user_id, group_id) values (55, 99  ,2);
insert into auth_user_groups (id, user_id, group_id) values (56, 100 ,2);
insert into auth_user_groups (id, user_id, group_id) values (57, 101 ,2);
insert into auth_user_groups (id, user_id, group_id) values (58, 102 ,2);
insert into auth_user_groups (id, user_id, group_id) values (59, 103 ,2);
insert into auth_user_groups (id, user_id, group_id) values (60, 104 ,2);
insert into auth_user_groups (id, user_id, group_id) values (61, 105 ,2);
insert into auth_user_groups (id, user_id, group_id) values (62, 106 ,2);
insert into auth_user_groups (id, user_id, group_id) values (63, 107 ,2);
insert into auth_user_groups (id, user_id, group_id) values (64, 108 ,2);
insert into auth_user_groups (id, user_id, group_id) values (65, 109 ,2);
insert into auth_user_groups (id, user_id, group_id) values (66, 110 ,2);
insert into auth_user_groups (id, user_id, group_id) values (67, 111 ,2);
insert into auth_user_groups (id, user_id, group_id) values (68, 112 ,2);
insert into auth_user_groups (id, user_id, group_id) values (69, 113 ,2);
insert into auth_user_groups (id, user_id, group_id) values (70, 114 ,2);
insert into auth_user_groups (id, user_id, group_id) values (71, 115 ,2);
insert into auth_user_groups (id, user_id, group_id) values (72, 116 ,2);
insert into auth_user_groups (id, user_id, group_id) values (73, 117 ,2);
insert into auth_user_groups (id, user_id, group_id) values (74, 118 ,2);
insert into auth_user_groups (id, user_id, group_id) values (75, 119 ,2);
insert into auth_user_groups (id, user_id, group_id) values (76, 120 ,2);
insert into auth_user_groups (id, user_id, group_id) values (77, 121 ,2);
insert into auth_user_groups (id, user_id, group_id) values (78, 122 ,2);
insert into auth_user_groups (id, user_id, group_id) values (79, 123 ,2);
insert into auth_user_groups (id, user_id, group_id) values (80, 124 ,2);
insert into auth_user_groups (id, user_id, group_id) values (81, 125 ,2);
insert into auth_user_groups (id, user_id, group_id) values (82, 126 ,2);
insert into auth_user_groups (id, user_id, group_id) values (83, 127 ,2);
insert into auth_user_groups (id, user_id, group_id) values (84, 128 ,2);
insert into auth_user_groups (id, user_id, group_id) values (85, 129 ,2);
insert into auth_user_groups (id, user_id, group_id) values (86, 130 ,2);
insert into auth_user_groups (id, user_id, group_id) values (87, 131 ,2);
insert into auth_user_groups (id, user_id, group_id) values (88, 132 ,2);
insert into auth_user_groups (id, user_id, group_id) values (89, 133 ,2);
insert into auth_user_groups (id, user_id, group_id) values (90, 134 ,2);
insert into auth_user_groups (id, user_id, group_id) values (91, 135 ,2);
insert into auth_user_groups (id, user_id, group_id) values (4 , 48  ,1);
insert into auth_user_groups (id, user_id, group_id) values (2 , 4   ,2);
insert into auth_user_groups (id, user_id, group_id) values (92, 138 ,2);


insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (1 ,   TRUE,   3  , 48);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (2 ,   TRUE,   4  , 49);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (3 ,   TRUE,   5  , 50);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (4 ,   TRUE,   6  , 51);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (5 ,   TRUE,   7  , 52);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (6 ,   TRUE,   8  , 53);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (7 ,   TRUE,   9  , 54);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (8 ,   TRUE,   10 , 55);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (9 ,   TRUE,   11 , 56);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (10,   TRUE,   12 , 57);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (11,   TRUE,   13 , 58);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (12,   TRUE,   14 , 59);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (13,   TRUE,   15 , 60);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (14,   TRUE,   16 , 61);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (15,   TRUE,   17 , 62);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (16,   TRUE,   18 , 63);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (17,   TRUE,   19 , 64);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (18,   TRUE,   20 , 65);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (19,   TRUE,   21 , 66);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (20,   TRUE,   22 , 67);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (21,   TRUE,   23 , 68);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (22,   TRUE,   24 , 69);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (23,   TRUE,   25 , 70);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (24,   TRUE,   26 , 71);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (25,   TRUE,   27 , 72);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (26,   TRUE,   28 , 73);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (27,   TRUE,   29 , 74);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (28,   TRUE,   30 , 75);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (29,   TRUE,   31 , 76);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (30,   TRUE,   32 , 77);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (31,   TRUE,   33 , 78);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (32,   TRUE,   34 , 79);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (33,   TRUE,   35 , 80);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (34,   TRUE,   36 , 81);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (35,   TRUE,   37 , 82);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (36,   TRUE,   38 , 83);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (37,   TRUE,   39 , 84);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (38,   TRUE,   40 , 85);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (39,   TRUE,   41 , 86);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (40,   TRUE,   42 , 87);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (41,   TRUE,   43 , 88);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (42,   TRUE,   44 , 89);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (43,   TRUE,   45 , 90);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (44,   TRUE,   46 , 91);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (45,   TRUE,   47 , 92);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (46,   TRUE,   48 , 93);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (47,   TRUE,   49 , 94);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (48,   TRUE,   50 , 95);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (49,   TRUE,   51 , 96);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (50,   TRUE,   52 , 97);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (51,   TRUE,   53 , 98);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (52 , TRUE,   54  ,100);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (53 , TRUE,   55  ,101);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (54 , TRUE,   56  ,102);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (55 , TRUE,   57  ,103);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (56 , TRUE,   58  ,104);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (57 , TRUE,   59  ,105);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (58 , TRUE,   60  ,106);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (59 , TRUE,   61  ,107);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (60 , TRUE,   62  ,108);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (61 , TRUE,   63  ,109);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (62 , TRUE,   64  ,110);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (63 , TRUE,   65  ,111);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (64 , TRUE,   66  ,112);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (65 , TRUE,   67  ,113);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (66 , TRUE,   68  ,114);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (67 , TRUE,   69  ,115);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (68 , TRUE,   70  ,116);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (69 , TRUE,   71  ,117);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (70 , TRUE,   72  ,118);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (71 , TRUE,   73  ,119);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (72 , TRUE,   74  ,120);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (73 , TRUE,   75  ,121);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (74 , TRUE,   76  ,122);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (75 , TRUE,   77  ,123);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (76 , TRUE,   78  ,124);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (77 , TRUE,   79  ,125);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (78 , TRUE,   80  ,126);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (79 , TRUE,   81  ,127);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (80 , TRUE,   82  ,128);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (81 , TRUE,   83  ,129);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (82 , TRUE,   84  ,130);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (83 , TRUE,   85  ,131);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (84 , TRUE,   86  ,132);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (85 , TRUE,   87  ,133);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (86 , TRUE,   88  ,134);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (87 , TRUE,   89  ,135);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (88,   TRUE,   90 , 99);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (89,   TRUE,   90,  4);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (91,   TRUE,   4 ,  3);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (92, FALSE,   90,  5);
insert into capacita_profile (id, permissao_necessidade, orgao_id, user_id) values (93, FALSE,   90  ,138);
END IF;
END
$do$
