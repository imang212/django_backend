## Django aplikace

Backend webová aplikace vytvořená pomocí django frameworku a sqlite databáze v rámci úkolu.

### Postup

Nejdřív si vytvořím django project například s názvem: todo_project, pak v todo_project složce startapp s názvem tasks.

Přešel jsem do vytvořené "tasks" složky Natavil model tabulky v databázi v models.py.

Udělám migraci, aby se mi vytvořila daná tabulka.

Udělal serializaci modelu pro nastavení vracení dat v serializers.py.

Přidal jsem GET metodu pro vrácení seznamu úkolů z databáze a další metody do views.py závislých na serializers.py a models.py.

Přidal jsem do urls.py cesty k daným metodám v tasks složce a zároveň i v todo_project složce do urls.py cestu do app a k django adminovi.

Udělal jsem si docker-compose a Dockerfile danému k projektu a spustil jsem ho v dockeru.

Tam jsem také musel umožnit migrace a vytvořil super uživatele.



### 1. úkol (GET)
Vrací na stránkách: "http://localhost:8000/tasks/" všechny úkoly z sqlite db.

### 2. úkol (POST)
Když pošlu úkol a uložím ho do sqlite databáze.
Vyzkoušel jsem ho pomocí spuštění python scriptu "make_post.py" ve složce projektu.
Následně jsem uložil do databáze úkol i s jeho obrázkém vybraným z měho PC, kde se v django složce uložil obrázek: "http://localhost:8000/media/tasks_photos/1013511" a můžu si ho na webu normálně otevřít. Zároveň i úkol mohu vidět na "http://localhost:8000/tasks/", kde mi ho to vrátí pomocí GET metody.
