# Integración Bitbucket + Jenkins

## Modelo recomendado

- Bitbucket es el repositorio principal y administra pull requests y restricciones.
- Jenkins Multibranch Pipeline descubre ramas y lee el `Jenkinsfile`.
- Bitbucket Pipelines ejecuta validaciones rápidas en pull requests.
- Jenkins ejecuta el pipeline completo y los despliegues.
- GitHub puede ser un espejo público de solo presentación.

## Webhook

Si Jenkins tiene un endpoint HTTPS protegido:

1. Instalar los plugins Bitbucket y Pipeline indicados por Ansible.
2. Crear un Multibranch Pipeline conectado al repositorio.
3. En Bitbucket, abrir Repository settings → Webhooks.
4. Configurar el endpoint publicado por el plugin de Jenkins.
5. Seleccionar eventos de push y pull request.
6. Crear un secreto y validar los envíos.

Si Jenkins permanece privado, iniciar con SCM polling. No abras el puerto 8080 a todo Internet únicamente para recibir webhooks.

## Credenciales

- Guardar el token de Bitbucket en Jenkins Credentials.
- Preferir un rol IAM de la instancia para AWS.
- No crear variables con claves AWS en el repositorio.
- No imprimir tokens ni respuestas de autenticación en el log del pipeline.

