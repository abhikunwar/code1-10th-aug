from app1 import run_app
import os

if __name__=="__main__":
    os.environ['ENV'] = 'testing'
    run_app() 




