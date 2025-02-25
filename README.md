## Django aplikace

Backend webová aplikace vytvořená pomocí django frameworku a sqlite databáze.

### 1. úkol (GET)
Vrací na stránkách: "localhost:8000/tasks/" všechny úkoly z sqlite db.

### 2. úkol (POST)
Když pošlu úkol a uložím ho do sqlite databáze.
Vyzkoušel jsem ho pomocí samostaatného python scriptu "app/make_post.py".
Následně jsem uložil do databáze úkol i s jeho obrázkém vybraným z měho PC, kde se v django složce uložil obrázek: "http://localhost:8000/media/tasks_photos/1013511" a můžu si ho na webu normálně otevřít. Zároveň i úkol mohu vidět na "http://localhost:8000/tasks/", kde mi ho to vrátí pomocí GET metody.
