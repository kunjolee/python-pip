import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return { 'name': 'Platzi' }

@app.get('/html', response_class=HTMLResponse)
def get_html():
    return"""
        <h2>This is a html title</h2>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()