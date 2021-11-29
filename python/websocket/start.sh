#uvicorn main:app --port=5021 --workers 5 &>/dev/null &
uvicorn main:app --reload --port=5000 --workers 1
#gunicorn main:app -b "127.0.0.1:5021"

