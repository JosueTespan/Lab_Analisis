PGDMP      %                }         	   contactos    17.4    17.4 -    ~           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            �           1262    16387 	   contactos    DATABASE     o   CREATE DATABASE contactos WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-SV';
    DROP DATABASE contactos;
                     postgres    false                        3079    16388 	   uuid-ossp 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
    DROP EXTENSION "uuid-ossp";
                        false            �           0    0    EXTENSION "uuid-ossp"    COMMENT     W   COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';
                             false    2            �            1259    16399 
   categorias    TABLE     �   CREATE TABLE public.categorias (
    idcategoria uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text
);
    DROP TABLE public.categorias;
       public         heap r       postgres    false    2            �            1259    16405 	   contactos    TABLE     �   CREATE TABLE public.contactos (
    idcontacto uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100),
    idcategoria uuid,
    idempresa uuid,
    fecha_nacimiento date
);
    DROP TABLE public.contactos;
       public         heap r       postgres    false    2            �            1259    16409    direcciones    TABLE     '  CREATE TABLE public.direcciones (
    iddireccion uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    direccion text NOT NULL,
    ciudad character varying(100),
    estado character varying(100),
    pais character varying(100),
    codigo_postal character varying(20)
);
    DROP TABLE public.direcciones;
       public         heap r       postgres    false    2            �            1259    16415    emails    TABLE     �   CREATE TABLE public.emails (
    idemail uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    tipo character varying(50),
    email character varying(150) NOT NULL
);
    DROP TABLE public.emails;
       public         heap r       postgres    false    2            �            1259    16419    empresas    TABLE     �   CREATE TABLE public.empresas (
    idempresa uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(150) NOT NULL,
    categoria character varying(100)
);
    DROP TABLE public.empresas;
       public         heap r       postgres    false    2            �            1259    16423 	   historial    TABLE     �   CREATE TABLE public.historial (
    idhistorial uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    descripcion text NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.historial;
       public         heap r       postgres    false    2            �            1259    16430    notas    TABLE     �   CREATE TABLE public.notas (
    idnota uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    nota text NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.notas;
       public         heap r       postgres    false    2            �            1259    16528    notificaciones    TABLE     U  CREATE TABLE public.notificaciones (
    id uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    fecha_envio timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
    estado text NOT NULL,
    CONSTRAINT notificaciones_estado_check CHECK ((estado = ANY (ARRAY['Pendiente'::text, 'Enviado'::text, 'Fallido'::text])))
);
 "   DROP TABLE public.notificaciones;
       public         heap r       postgres    false    2            �            1259    16437    recordatorios    TABLE       CREATE TABLE public.recordatorios (
    idrecordatorio uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    descripcion text NOT NULL,
    fecha_recordatorio timestamp without time zone NOT NULL,
    completado boolean DEFAULT false
);
 !   DROP TABLE public.recordatorios;
       public         heap r       postgres    false    2            �            1259    16444 	   telefonos    TABLE     �   CREATE TABLE public.telefonos (
    idtelefono uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    tipo character varying(50),
    numero character varying(20) NOT NULL
);
    DROP TABLE public.telefonos;
       public         heap r       postgres    false    2            r          0    16399 
   categorias 
   TABLE DATA           F   COPY public.categorias (idcategoria, nombre, descripcion) FROM stdin;
    public               postgres    false    218   �8       s          0    16405 	   contactos 
   TABLE DATA           k   COPY public.contactos (idcontacto, nombre, apellido, idcategoria, idempresa, fecha_nacimiento) FROM stdin;
    public               postgres    false    219   �9       t          0    16409    direcciones 
   TABLE DATA           n   COPY public.direcciones (iddireccion, idcontacto, direccion, ciudad, estado, pais, codigo_postal) FROM stdin;
    public               postgres    false    220   �:       u          0    16415    emails 
   TABLE DATA           B   COPY public.emails (idemail, idcontacto, tipo, email) FROM stdin;
    public               postgres    false    221   �;       v          0    16419    empresas 
   TABLE DATA           @   COPY public.empresas (idempresa, nombre, categoria) FROM stdin;
    public               postgres    false    222   �<       w          0    16423 	   historial 
   TABLE DATA           P   COPY public.historial (idhistorial, idcontacto, descripcion, fecha) FROM stdin;
    public               postgres    false    223   {=       x          0    16430    notas 
   TABLE DATA           @   COPY public.notas (idnota, idcontacto, nota, fecha) FROM stdin;
    public               postgres    false    224   �>       {          0    16528    notificaciones 
   TABLE DATA           M   COPY public.notificaciones (id, idcontacto, fecha_envio, estado) FROM stdin;
    public               postgres    false    227   �?       y          0    16437    recordatorios 
   TABLE DATA           p   COPY public.recordatorios (idrecordatorio, idcontacto, descripcion, fecha_recordatorio, completado) FROM stdin;
    public               postgres    false    225   �A       z          0    16444 	   telefonos 
   TABLE DATA           I   COPY public.telefonos (idtelefono, idcontacto, tipo, numero) FROM stdin;
    public               postgres    false    226   �B       �           2606    16449     categorias categorias_nombre_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_nombre_key UNIQUE (nombre);
 J   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_nombre_key;
       public                 postgres    false    218            �           2606    16451    categorias categorias_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (idcategoria);
 D   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_pkey;
       public                 postgres    false    218            �           2606    16453    contactos contactos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_pkey PRIMARY KEY (idcontacto);
 B   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_pkey;
       public                 postgres    false    219            �           2606    16455    direcciones direcciones_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_pkey PRIMARY KEY (iddireccion);
 F   ALTER TABLE ONLY public.direcciones DROP CONSTRAINT direcciones_pkey;
       public                 postgres    false    220            �           2606    16457    emails emails_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.emails
    ADD CONSTRAINT emails_pkey PRIMARY KEY (idemail);
 <   ALTER TABLE ONLY public.emails DROP CONSTRAINT emails_pkey;
       public                 postgres    false    221            �           2606    16459    empresas empresas_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.empresas
    ADD CONSTRAINT empresas_pkey PRIMARY KEY (idempresa);
 @   ALTER TABLE ONLY public.empresas DROP CONSTRAINT empresas_pkey;
       public                 postgres    false    222            �           2606    16461    historial historial_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_pkey PRIMARY KEY (idhistorial);
 B   ALTER TABLE ONLY public.historial DROP CONSTRAINT historial_pkey;
       public                 postgres    false    223            �           2606    16463    notas notas_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_pkey PRIMARY KEY (idnota);
 :   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_pkey;
       public                 postgres    false    224            �           2606    16537 "   notificaciones notificaciones_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.notificaciones
    ADD CONSTRAINT notificaciones_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.notificaciones DROP CONSTRAINT notificaciones_pkey;
       public                 postgres    false    227            �           2606    16465     recordatorios recordatorios_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.recordatorios
    ADD CONSTRAINT recordatorios_pkey PRIMARY KEY (idrecordatorio);
 J   ALTER TABLE ONLY public.recordatorios DROP CONSTRAINT recordatorios_pkey;
       public                 postgres    false    225            �           2606    16467    telefonos telefonos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.telefonos
    ADD CONSTRAINT telefonos_pkey PRIMARY KEY (idtelefono);
 B   ALTER TABLE ONLY public.telefonos DROP CONSTRAINT telefonos_pkey;
       public                 postgres    false    226            �           2606    16468 $   contactos contactos_idcategoria_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_idcategoria_fkey FOREIGN KEY (idcategoria) REFERENCES public.categorias(idcategoria);
 N   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_idcategoria_fkey;
       public               postgres    false    218    4806    219            �           2606    16473 "   contactos contactos_idempresa_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_idempresa_fkey FOREIGN KEY (idempresa) REFERENCES public.empresas(idempresa);
 L   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_idempresa_fkey;
       public               postgres    false    222    219    4814            �           2606    16508 '   direcciones direcciones_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto) ON DELETE CASCADE;
 Q   ALTER TABLE ONLY public.direcciones DROP CONSTRAINT direcciones_idcontacto_fkey;
       public               postgres    false    220    4808    219            �           2606    16538    notificaciones fk_contacto    FK CONSTRAINT     �   ALTER TABLE ONLY public.notificaciones
    ADD CONSTRAINT fk_contacto FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 D   ALTER TABLE ONLY public.notificaciones DROP CONSTRAINT fk_contacto;
       public               postgres    false    219    4808    227            �           2606    16488 #   historial historial_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 M   ALTER TABLE ONLY public.historial DROP CONSTRAINT historial_idcontacto_fkey;
       public               postgres    false    223    4808    219            �           2606    16493    notas notas_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 E   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_idcontacto_fkey;
       public               postgres    false    4808    219    224            �           2606    16498 +   recordatorios recordatorios_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.recordatorios
    ADD CONSTRAINT recordatorios_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 U   ALTER TABLE ONLY public.recordatorios DROP CONSTRAINT recordatorios_idcontacto_fkey;
       public               postgres    false    225    219    4808            �           2606    16503 #   telefonos telefonos_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.telefonos
    ADD CONSTRAINT telefonos_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 M   ALTER TABLE ONLY public.telefonos DROP CONSTRAINT telefonos_idcontacto_fkey;
       public               postgres    false    219    226    4808            r   �   x�U�1r� F�N�6b�Τw�2����IF6
�s~�L�W}���- ��B��L�3ρ��5�������wq?O��o������臍s.[�Pb ֵВ�ҼTp���e�_@��g�u���U��i%� �rIʍR(������m� ��uH�ﳆS�M�5b?߬�/�D�      s   :  x���1n\1Dk��� )J�J��;�M#RT����ڍO�2H�b8�f���1��h�к�ZcL�A������6��_�b�a�=G��v0H�4\8)�;/��@�R�T�VM����Q�����g!�ƶ Ze���H�q�|���~�^S�>3�i��Lض���1�\�庬�Z�lc��`���=�I�'*0��p�@����D�Y���>�=}��ϸ&�!�� �Ǝ�K�R
i1����z�Uw=���ղ}�}-,�4���CCj�����E:�S��jI��'G<�+ɯ��8��8��      t     x����j�0Dk�+[��>$K*H���m��q�����(]R�N10��:ef N�A�V �ӂ!�'1NrN��z�$B*���kJ؊5����t���:�e�H�x�n2�mݷ5ݴ�r��f���{��հ�0�����6S��:�����q^mC/0��!w"_[�0��;��\����Ӷ��y�y�!��!݀-�k|�`U2� ;�X}Cr�OlKr�ɺ~�T��iB�TmU2��xJ�����m�;����WZ�_"���8�7z�r�      u   �   x�m��j�@е�/2�4�]7��n�H�&P���:�@@���d(�3�	A��0zA�4V��ZM�Y1����:%� �8y���_�_o��c;�����d�%�X����5���!�]ah�p$]�O�U�csN@)w���	��ŋ��ן7cu!�`�������CƊd��#�J<����)U�Z��&���x��<���d�      v   �   x��1�  ��%���lG�$�K����Sx1Y��'U�$8P$�@-�0��)�8_�R��C}o���}�
R��B��;�݌IBFs=�M�^�Yv~�϶Պ�95ʠZ���$����:�����e�>.��?�^0N      w     x�}�=n�0��>�.�����l�AѹEQ@��*;C��#�bUС[�|���)&��1 -��d��5�ѥ)E�H؃2y��TH�,��+U�Ӌ�_/_,����T5ҷM�ѫʾ��E���y@\��gg��Ms����m`% c�,�Dd�;/q�K)�1�To�쒁E��Zl��ӛ�/�źo�w���=xV7�B�����3$WR�&��O>*5�} ����H6�&6���^����v`s�f=���硷�r��s��i��_��q�      x   $  x�}�=��0���>�.�%Qӧ��P�ر�L�)��Ţ] m��x��ұzn �#P�-R�^��Z�beI�wnXAF�@>6`� ޒ�G]���O�q�N��=^�������^O�t�{����%`H�]�7�7�7_����B��u�ҡ�lS�;͆�K*J�%B�T��g�2L|͖KZ�����p�N�!���$^���?��]���~p�>�z��߲o���ԧ2B<�[1�j�����K->�peJ@%��<XΈ�EC��!��>X�c��Bt��ϭ���u�Dmy%      {     x��U��1�w�p4x����'�(N�����-� �@J��w��]�qC�e0�e�R�M�\t|Oz��q��(��!�o�u7�]s}1� �����~���{�߷�S�&�è���
K���9
�`����&���)@gs�k$C�@���FxaX�\���ž�9J��B�%#� ����H���Q�n�7tQ�r\!.��+��о�����&o0=݀u�������]�[�E�ڳ�rE��$yN�<&E�e/����)
���`�j����&��F3f4c��0a2mݕ't?��X>� �@�B{�@3.om�]�IQn�R�[a0g*��(�҅���օ/�\Q:���Tn�h͓�jƬ����8�T�Cv>G���/�`I��X�K]0d��I�z �Ɯ���
�Ֆ��WzC��'���9��@�J�ޅ� �0l�#p�Τ9�.�V,j�R�<���9���G�}�`��"t�7��H�灼���pW��;1`αaa�+����������      y      x�M�Mj1�מS�T$[���(]w#�rH'!I{���%��=��B�э+�.�D@<50�R�f��d��n�3�C�R�`��hҹ��|�e=�E֫�n������# �Jx�����V9��XL�I:4�2]M��"�bhM*�i�D��8�p���W�ڮ����v[���.�W�Ւ��Z��{��A8�\�jAs
.f�9@�;իBi�Q�C���rt/Gٷ���X�,�ݦf������oO˲��a�      z   X   x��A�0�u{L���������'��j��9NCX�������e|���Tm-=$������Ln�\����m@     