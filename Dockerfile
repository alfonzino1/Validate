FROM python:3.12-slim as builder
WORKDIR /app
COPY validate.py .


FROM python:3.12-slim
WORKDIR /app
RUN useradd -m -u 1000 appuser
USER appuser
COPY --chown=appuser:appuser --from=builder /app/validate.py .
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD python -c "print('OK')"
CMD ["python","validate.py"]