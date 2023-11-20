# ChatterBot Bob

Pour l'instant sous forme de .py, simplement le run et communiquer dans le terminal


## Dépendances :

run sur python 3.6.8

pip install spacy

pip install chatterbot

pip install chatterbot-corpus *(non testé)*

ou

https://github.com/gunthercox/chatterbot-corpus

## Lib modifications :

### chatterbot > corpus > line 9 : 
```python
except (ImportError, ModuleNotFoundError):
    # Default to the home directory of the current user
    DATA_DIRECTORY = os.path.join(
        Path.home(),
        'Desktop',
        'interaction-distribuee',
        'ChatterBot',
        'chatterbot-corpus',
        'chatterbot-corpus',
        'data'
    )
```
remplacer par le chemin vers le chatter-bot corpus, cloné depuis :         
https://github.com/gunthercox/chatterbot-corpus

### chatterbot > langages > line 584 : 
```python 
ISO_639_1 = 'en_core_web_sm'
```
