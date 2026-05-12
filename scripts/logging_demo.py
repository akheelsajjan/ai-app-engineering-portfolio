import logging


logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def process_ticket(ticket_id: int):
    logger.info(f"Processing ticket {ticket_id}")

    if ticket_id == 404:
        logger.error("Ticket not found")
        return

    logger.info("Ticket processed successfully")


def main():
    process_ticket(101)
    process_ticket(404)


if __name__ == "__main__":
    main()