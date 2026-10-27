# sempre-magra-posts

Imagens públicas dos carrosséis do Instagram **@sempremaagra**, geradas e publicadas automaticamente 3 vezes por dia (7h, 12h e 21h, horário de Brasília).

- `GUIA.md`: regras de conteúdo, tom de voz e estrutura dos slides
- `kit.py`: transforma `posts/<id>/post.json` nos 7 slides JPEG (1080×1350)
- `ilus.py`: ilustrações da marca
- `historico.md`: registro de tudo o que já foi publicado
- `posts/<id>/`: cada post, com `post.json`, `legenda.txt` e `slide-1.jpg` a `slide-7.jpg`
- `exemplo/`: um post-modelo completo

As imagens ficam públicas em `https://raw.githubusercontent.com/dmullergestor-prog/sempre-magra-posts/main/posts/<id>/slide-N.jpg`.
