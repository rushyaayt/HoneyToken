import logging
import requests

logger = logging.getLogger("honeytoken.alert")


def send_alert(webhook_url: str, payload: dict):
    try:
        resp = requests.post(webhook_url, json=payload, timeout=5)
        resp.raise_for_status()
    except Exception as e:
        logger.exception("Failed sending alert: %s", e)
