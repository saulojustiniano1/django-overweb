# ARQUIVOS ESTÁTICOS NO DJANGO

## O que são arquivos estáticos?

Arquivos estáticos são arquivos que não são processados pelo servidor antes de serem enviados para o cliente. Eles são enviados exatamente como estão no servidor. Exemplos de arquivos estáticos são arquivos de imagem, arquivos de estilo CSS, arquivos de script JavaScript, arquivos de fonte, etc.

## Configuração de arquivos estáticos

Para configurar arquivos estáticos no Django, você precisa seguir os seguintes passos:

1. Adicione o diretório de arquivos estáticos ao arquivo de configuração `settings.py` do seu projeto Django. Para fazer isso, adicione a seguinte linha ao arquivo `settings.py`:

```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

2. Crie um diretório chamado `static` na raiz do seu projeto Django. Este diretório é onde você colocará todos os seus arquivos estáticos.

3. Para acessar arquivos estáticos em seus modelos, você pode usar a tag `{% static %}`. Por exemplo, se você quiser acessar um arquivo de imagem chamado `logo.png` em um modelo, você pode fazer o seguinte:

```html
<img src="{% static 'logo.png' %}" alt="Logo" />
```

4. Para acessar arquivos estáticos em seus arquivos CSS e JavaScript, você pode usar a função `static` do Django. Por exemplo, se você quiser acessar um arquivo de imagem chamado `logo.png` em um arquivo CSS, você pode fazer o seguinte:

```css
.logo {
  background-image: url("{% static 'logo.png' %}");
}
```

5. Para coletar arquivos estáticos em um diretório específico, você pode usar o comando `collectstatic` do Django. Por exemplo, se você quiser coletar todos os arquivos estáticos em um diretório chamado `staticfiles`, você pode fazer o seguinte:

```bash
python manage.py collectstatic
```

## Conclusão

Arquivos estáticos são uma parte importante de qualquer aplicação web. Eles são usados para fornecer estilos, scripts e imagens para a aplicação. Configurar arquivos estáticos no Django é fácil e direto. Basta seguir os passos acima e você estará pronto para começar a usar arquivos estáticos em seu projeto Django.

## Vídeo

Você pode assistir ao vídeo relacionado a este tópico no seguinte

link: <https://www.youtube.com/watch?v=AWIJ2uMRjS0>
