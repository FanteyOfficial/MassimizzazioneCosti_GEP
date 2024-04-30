### pyinstaller command:
Da eseguire con venv attivo e immagino con le apposite librerie installate
```cmd
venv\Scripts\activate
pyinstaller --noconfirm --onefile --console --add-data "D:\ProgrammingFolder\Python\MassimizzazioneCosti_GEP\venv\Lib\site-packages\pulp;pulp/"  "LocalInterface.py"
```

Restrizioni:
- I vincoli devono essere formule scritte in maniera esplicita (semplificate)
Esempi:<br/>
2*x - 7*y + 3 <= 15 -> NO
<br/>
2*x - 7*y <= 12 -> Sì (abbiamo fatto direttamente 15 - 3 in questo caso)

Esempio di caso funzionante:

```txt
    z = 20* x + 12.5 *y
    0.72*x + 0.23*y <= 13
    2*x + 0.2*y <= 31
    12*x + 3*y <= 230
    0.33*x + 0.28*y <= 10
```