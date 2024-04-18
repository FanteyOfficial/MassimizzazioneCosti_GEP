### pyinstaller command:
Da eseguire con venv attivo e immagino con le apposite librerie installate
```cmd
venv\Scripts\activate
pyinstaller --noconfirm --onefile --console --add-data "D:\ProgrammingFolder\Python\MassimizzazioneCosti_GEP\venv\Lib\site-packages\pulp;pulp/"  "LocalInterface.py"
```