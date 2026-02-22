from datetime import datetime, timezone


def main() -> None:
    print("fraud-detection-real-time-streams initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
