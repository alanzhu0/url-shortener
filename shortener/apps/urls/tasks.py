from typing import List
from datetime import timedelta

from celery import shared_task

from django.conf import settings
from django.utils.timezone import now

from .emails import email_send
from .models import URL


@shared_task
def send_action_emails(
    url_ids: List[int], action: str, subject: str, host: str = ""
) -> None:
    urls = URL.objects.filter(id__in=url_ids)
    for url in urls:
        email_send(
            f"emails/{action}.txt",
            f"emails/{action}.html",
            {"url": url, "host": host, "dev_email": settings.DEVELOPER_EMAIL},
            subject,
            [url.created_by.email],
        )


@shared_task
def delete_old_urls() -> None:
    qs = URL.objects.filter(created_at__lt=now() - timedelta(weeks=26))
    send_action_emails(
        [x.id for x in qs], "deletion", "Short URL Deleted"
    )  # Must be regular function call b/c objects get deleted afterwards
    qs.delete()
