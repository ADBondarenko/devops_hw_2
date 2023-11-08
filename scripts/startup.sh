#In case built-in Render.com shell fails

uvicorn main:app --host 0.0.0.0 --port $PORT
