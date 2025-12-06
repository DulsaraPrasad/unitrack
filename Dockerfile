FROM heroku/heroku:24-build as builder

COPY requirements.txt .
RUN pip install -r requirements.txt --user

FROM heroku/heroku:24

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

ENV PATH=/root/.local/bin:$PATH
ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:${PORT}"]
