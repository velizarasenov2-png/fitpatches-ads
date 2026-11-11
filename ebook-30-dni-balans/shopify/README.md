# Е-книгата като подарък в Shopify

- Продукт: `/products/e-kniga-30-dni-balans` (0 €, зачертано 19,99 €, без доставка, скрит от търсенето).
- PDF: Shopify Files → `30-dni-balans-FitPatches.pdf`.
- Тема (копие): „FitPatches — е-книга подарък 11.11 (ПУБЛИКУВАЙ)“.

Файлове в темата (`snippets/`):
- `fp-ebook-gift.liquid` (нов): лента „+ ПОДАРЪК“ в офертите 2+1 и 3+2; е-книгата влиза/излиза от количката сама (3+ пакета); ред „Безплатно“ в количката.
- `fp-ebook-thanks.liquid` (нов): бутон „Изтегли е-книгата“ на /pages/thank-you.
- `fp-quick-es.liquid`: добавен `{% render 'fp-ebook-gift' %}`.
- `fp-thanks.liquid`: добавен `{% render 'fp-ebook-thanks' %}`.

Демо на страницата „Благодарим“: `/pages/thank-you?fp_demo=1&ebook=1&t=39.99`

`preview_proxy.py`: локален преглед на непубликувана тема (`python3 preview_proxy.py 8080 <theme_id>`).
