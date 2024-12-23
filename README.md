![image](https://github.com/user-attachments/assets/3764a910-b857-4d8f-adf3-490aac121150)
![image](https://github.com/user-attachments/assets/0d06e051-abaf-4f1a-ac08-9f2c3dc62a0d)


**PASOS A SEGUIR**

1. **Abre Instagram**
   - Ve a [https://www.instagram.com](https://www.instagram.com).
   - Haz clic derecho en cualquier parte de la página y selecciona **"Inspeccionar"**.
   - ![image](https://github.com/user-attachments/assets/99f81546-545d-4ed2-b5cf-290937d1dcf0)


2. **Accede a la sección "Aplicación"**
   - En la parte superior de las herramientas de desarrollo, busca la pestaña **"Aplicación"**.
   - Si no la encuentras, desplázate hacia la derecha en el menú hasta verla.
   - ![image](https://github.com/user-attachments/assets/aef577d7-decd-49f0-9d93-b39dba3d46c7)


3. **Encuentra las Cookies**
   - Dentro de la sección "Aplicación", en el menú lateral, busca **"Almacenamiento"** y selecciona **"Cookies"**.
   - Aparecerá una lista de dominios, selecciona el dominio que corresponde a Instagram.

4. **Localiza el "sessionid"**
   - Dentro de las cookies del dominio, busca la clave llamada **"sessionid"**.
   - Copia el contenido que aparece en la columna de "Valor" para esta clave.

5. **Sustituye el valor en el código**
   - Ve al archivo `Tool IG.py` en tu repositorio de GitHub en la línea 19:
     [https://github.com/Kayy9961/InstagramMessageTool/blob/26fefc5effa19d666a44315c0a756db84af7417f/Tool%20IG.py#L19](https://github.com/Kayy9961/InstagramMessageTool/blob/26fefc5effa19d666a44315c0a756db84af7417f/Tool%20IG.py#L19)
   - Sustituye el valor del **"sessionid"** por el que acabas de copiar.
   - ![image](https://github.com/user-attachments/assets/6791bf2a-bc38-4b3d-88a9-b51e101b1011)


6. **¡Listo!**
   - Guarda los cambios en el archivo.
   - Ahora tu herramienta está configurada correctamente.
