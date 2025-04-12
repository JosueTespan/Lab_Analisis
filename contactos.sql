PGDMP  %    !        
        }         	   contactos    17.4    17.4 *    t           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                           false            u           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                           false            v           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                           false            w           1262    16387 	   contactos    DATABASE     o   CREATE DATABASE contactos WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'es-SV';
    DROP DATABASE contactos;
                     postgres    false                        3079    16388 	   uuid-ossp 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;
    DROP EXTENSION "uuid-ossp";
                        false            x           0    0    EXTENSION "uuid-ossp"    COMMENT     W   COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';
                             false    2            �            1259    16475 
   categorias    TABLE     �   CREATE TABLE public.categorias (
    idcategoria uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion text
);
    DROP TABLE public.categorias;
       public         heap r       postgres    false    2            �            1259    16491 	   contactos    TABLE     �   CREATE TABLE public.contactos (
    idcontacto uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(100) NOT NULL,
    apellido character varying(100),
    idcategoria uuid,
    idempresa uuid,
    fecha_nacimiento date
);
    DROP TABLE public.contactos;
       public         heap r       postgres    false    2            �            1259    16507    direcciones    TABLE     '  CREATE TABLE public.direcciones (
    iddireccion uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    direccion text NOT NULL,
    ciudad character varying(100),
    estado character varying(100),
    pais character varying(100),
    codigo_postal character varying(20)
);
    DROP TABLE public.direcciones;
       public         heap r       postgres    false    2            �            1259    16531    emails    TABLE     �   CREATE TABLE public.emails (
    idemail uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    tipo character varying(50),
    email character varying(150) NOT NULL
);
    DROP TABLE public.emails;
       public         heap r       postgres    false    2            �            1259    16485    empresas    TABLE     �   CREATE TABLE public.empresas (
    idempresa uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    nombre character varying(150) NOT NULL,
    categoria character varying(100)
);
    DROP TABLE public.empresas;
       public         heap r       postgres    false    2            �            1259    16570 	   historial    TABLE     �   CREATE TABLE public.historial (
    idhistorial uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    descripcion text NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.historial;
       public         heap r       postgres    false    2            �            1259    16542    notas    TABLE     �   CREATE TABLE public.notas (
    idnota uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    nota text NOT NULL,
    fecha timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.notas;
       public         heap r       postgres    false    2            �            1259    16556    recordatorios    TABLE       CREATE TABLE public.recordatorios (
    idrecordatorio uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    descripcion text NOT NULL,
    fecha_recordatorio timestamp without time zone NOT NULL,
    completado boolean DEFAULT false
);
 !   DROP TABLE public.recordatorios;
       public         heap r       postgres    false    2            �            1259    16520 	   telefonos    TABLE     �   CREATE TABLE public.telefonos (
    idtelefono uuid DEFAULT public.uuid_generate_v4() NOT NULL,
    idcontacto uuid,
    tipo character varying(50),
    numero character varying(20) NOT NULL
);
    DROP TABLE public.telefonos;
       public         heap r       postgres    false    2            i          0    16475 
   categorias 
   TABLE DATA           F   COPY public.categorias (idcategoria, nombre, descripcion) FROM stdin;
    public               postgres    false    218   u4       k          0    16491 	   contactos 
   TABLE DATA           k   COPY public.contactos (idcontacto, nombre, apellido, idcategoria, idempresa, fecha_nacimiento) FROM stdin;
    public               postgres    false    220   45       l          0    16507    direcciones 
   TABLE DATA           n   COPY public.direcciones (iddireccion, idcontacto, direccion, ciudad, estado, pais, codigo_postal) FROM stdin;
    public               postgres    false    221   b6       n          0    16531    emails 
   TABLE DATA           B   COPY public.emails (idemail, idcontacto, tipo, email) FROM stdin;
    public               postgres    false    223   ~7       j          0    16485    empresas 
   TABLE DATA           @   COPY public.empresas (idempresa, nombre, categoria) FROM stdin;
    public               postgres    false    219   c8       q          0    16570 	   historial 
   TABLE DATA           P   COPY public.historial (idhistorial, idcontacto, descripcion, fecha) FROM stdin;
    public               postgres    false    226   9       o          0    16542    notas 
   TABLE DATA           @   COPY public.notas (idnota, idcontacto, nota, fecha) FROM stdin;
    public               postgres    false    224   :       p          0    16556    recordatorios 
   TABLE DATA           p   COPY public.recordatorios (idrecordatorio, idcontacto, descripcion, fecha_recordatorio, completado) FROM stdin;
    public               postgres    false    225   Z;       m          0    16520 	   telefonos 
   TABLE DATA           I   COPY public.telefonos (idtelefono, idcontacto, tipo, numero) FROM stdin;
    public               postgres    false    222   j<       �           2606    16484     categorias categorias_nombre_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_nombre_key UNIQUE (nombre);
 J   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_nombre_key;
       public                 postgres    false    218            �           2606    16482    categorias categorias_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.categorias
    ADD CONSTRAINT categorias_pkey PRIMARY KEY (idcategoria);
 D   ALTER TABLE ONLY public.categorias DROP CONSTRAINT categorias_pkey;
       public                 postgres    false    218            �           2606    16496    contactos contactos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_pkey PRIMARY KEY (idcontacto);
 B   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_pkey;
       public                 postgres    false    220            �           2606    16514    direcciones direcciones_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_pkey PRIMARY KEY (iddireccion);
 F   ALTER TABLE ONLY public.direcciones DROP CONSTRAINT direcciones_pkey;
       public                 postgres    false    221            �           2606    16536    emails emails_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.emails
    ADD CONSTRAINT emails_pkey PRIMARY KEY (idemail);
 <   ALTER TABLE ONLY public.emails DROP CONSTRAINT emails_pkey;
       public                 postgres    false    223            �           2606    16490    empresas empresas_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.empresas
    ADD CONSTRAINT empresas_pkey PRIMARY KEY (idempresa);
 @   ALTER TABLE ONLY public.empresas DROP CONSTRAINT empresas_pkey;
       public                 postgres    false    219            �           2606    16578    historial historial_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_pkey PRIMARY KEY (idhistorial);
 B   ALTER TABLE ONLY public.historial DROP CONSTRAINT historial_pkey;
       public                 postgres    false    226            �           2606    16550    notas notas_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_pkey PRIMARY KEY (idnota);
 :   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_pkey;
       public                 postgres    false    224            �           2606    16564     recordatorios recordatorios_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.recordatorios
    ADD CONSTRAINT recordatorios_pkey PRIMARY KEY (idrecordatorio);
 J   ALTER TABLE ONLY public.recordatorios DROP CONSTRAINT recordatorios_pkey;
       public                 postgres    false    225            �           2606    16525    telefonos telefonos_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.telefonos
    ADD CONSTRAINT telefonos_pkey PRIMARY KEY (idtelefono);
 B   ALTER TABLE ONLY public.telefonos DROP CONSTRAINT telefonos_pkey;
       public                 postgres    false    222            �           2606    16497 $   contactos contactos_idcategoria_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_idcategoria_fkey FOREIGN KEY (idcategoria) REFERENCES public.categorias(idcategoria);
 N   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_idcategoria_fkey;
       public               postgres    false    218    220    4799            �           2606    16502 "   contactos contactos_idempresa_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.contactos
    ADD CONSTRAINT contactos_idempresa_fkey FOREIGN KEY (idempresa) REFERENCES public.empresas(idempresa);
 L   ALTER TABLE ONLY public.contactos DROP CONSTRAINT contactos_idempresa_fkey;
       public               postgres    false    4801    219    220            �           2606    16515 '   direcciones direcciones_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.direcciones
    ADD CONSTRAINT direcciones_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 Q   ALTER TABLE ONLY public.direcciones DROP CONSTRAINT direcciones_idcontacto_fkey;
       public               postgres    false    220    4803    221            �           2606    16537    emails emails_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.emails
    ADD CONSTRAINT emails_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 G   ALTER TABLE ONLY public.emails DROP CONSTRAINT emails_idcontacto_fkey;
       public               postgres    false    223    4803    220            �           2606    16579 #   historial historial_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.historial
    ADD CONSTRAINT historial_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 M   ALTER TABLE ONLY public.historial DROP CONSTRAINT historial_idcontacto_fkey;
       public               postgres    false    4803    226    220            �           2606    16551    notas notas_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 E   ALTER TABLE ONLY public.notas DROP CONSTRAINT notas_idcontacto_fkey;
       public               postgres    false    224    220    4803            �           2606    16565 +   recordatorios recordatorios_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.recordatorios
    ADD CONSTRAINT recordatorios_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 U   ALTER TABLE ONLY public.recordatorios DROP CONSTRAINT recordatorios_idcontacto_fkey;
       public               postgres    false    220    4803    225            �           2606    16526 #   telefonos telefonos_idcontacto_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.telefonos
    ADD CONSTRAINT telefonos_idcontacto_fkey FOREIGN KEY (idcontacto) REFERENCES public.contactos(idcontacto);
 M   ALTER TABLE ONLY public.telefonos DROP CONSTRAINT telefonos_idcontacto_fkey;
       public               postgres    false    4803    222    220            i   �   x�U�1r� F�N�6b�Τw�2����IF6
�s~�L�W}���- ��B��L�3ρ��5�������wq?O��o������臍s.[�Pb ֵВ�ҼTp���e�_@��g�u���U��i%� �rIʍR(������m� ��uH�ﳆS�M�5b?߬�/�D�      k     x��1ND1D���ىc'%��Z��q�J�_Z���d;�7Ӕ2���+��	�3�A�1y����7��9o����K1Ѱb�^"��v0��1.���=/c/b��:���D���3eD�|�b6:6�Y	�J��-�V]A�<<�K�._�->/�k*�gW -�c���.`<�-K�dE��]��m�Ql ��`/j��#*�|T^�$����t.�&K����u^���t�~�l�U�@;cO1�8T�j��=���Kv?��I� [��Vw9�A����p�? {kp      l     x����jAE�ٯXp� i4�2�t��M3MXXv����g�n�).��$m����|�T��������Xjv�YH�b��=��&Mɼ>^�s>�����2�Dl�uߎ}�w������u�����~3DHSQ_��q�QO��
X�V�EY�l)9a����M�ke����U�����#��|�-[]~�:���','錌!CE� �"$T�{_�a3.�t��[p�� 
�W����̧K�1?���1_�m�S�鉇u覯�i�� Ts�      n   �   x�m��j�@е�/2�4�]7��n�H�&P���:�@@���d(�3�	A��0zA�4V��ZM�Y1����:%� �8y���_�_o��c;�����d�%�X����5���!�]ah�p$]�O�U�csN@)w���	��ŋ��ן7cu!�`�������CƊd��#�J<����)U�Z��&���x��<���d�      j   �   x��1�  ��%���lG�$�K����Sx1Y��'U�$8P$�@-�0��)�8_�R��C}o���}�
R��B��;�݌IBFs=�M�^�Yv~�϶Պ�95ʠZ���$����:�����e�>.��?�^0N      q     x�}�=n�0��>�.�����l�AѹEQ@��*;C��#�bUС[�|���)&��1 -��d��5�ѥ)E�H؃2y��TH�,��+U�Ӌ�_/_,����T5ҷM�ѫʾ��E���y@\��gg��Ms����m`% c�,�Dd�;/q�K)�1�To�쒁E��Zl��ӛ�/�źo�w���=xV7�B�����3$WR�&��O>*5�} ����H6�&6���^����v`s�f=���硷�r��s��i��_��q�      o   .  x�}нm�@��Z�B������3@�L�:C��d�̑�r� �>,�F�D�SAI>a	&�␢��!������3�! 
UW�/�Y�]�O*�~���m��|?o�*�.�T�-�N��q2''tG�\��`�`2��3Yp�3d�&(Q��5ޖBp����<�Q�bPYX���}�Զ>4��r�͕�Xeۉ��(���|�S�Vv�����0H!h����E��Gq��B�;jb�T�2�*�4D?�^��^�=�,��>���ݺ�r]�e����(���z��//3?'���?���      p      x�M�Mj1�מS�T$[���(]w#�rH'!I{���%��=��B�э+�.�D@<50�R�f��d��n�3�C�R�`��hҹ��|�e=�E֫�n������# �Jx�����V9��XL�I:4�2]M��"�bhM*�i�D��8�p���W�ڮ����v[���.�W�Ւ��Z��{��A8�\�jAs
.f�9@�;իBi�Q�C���rt/Gٷ���X�,�ݦf������oO˲��a�      m   �   x�U��m�1�ϻ��`�R��Y,#d�8��=��N�i��u�h���,��9�Q�A���@2���{yR>�?ߟ_�t0�W3�'�s�q��
�jH3s><�v�<��]��)�'*�E-j���k��t�͠u�jL��{/����t���_="@�](yu�%�����>�Zk&H�     