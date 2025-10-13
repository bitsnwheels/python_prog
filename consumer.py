# consumer.py
import argparse, json
from kafka import KafkaConsumer

ALERT_THRESHOLD = 150.0

def to_float(x):
    try:
        return float(x)
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser(description="Kafka air quality consumer")
    ap.add_argument("--bootstrap-server", default="localhost:9092")
    ap.add_argument("--topic", default="air_quality")
    ap.add_argument("--group-id", default="air-quality-consumers")
    args = ap.parse_args()

    consumer = KafkaConsumer(
        args.topic,
        bootstrap_servers=args.bootstrap_server,
        group_id=args.group_id,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode("utf-8")),
        key_deserializer=lambda v: v.decode("utf-8") if v else None,
    )

    print(f"Listening on topic '{args.topic}'… Press Ctrl+C to stop.")
    for msg in consumer:
        data = msg.value or {}
        key = msg.key
        pm25 = data.get("pm25")
        pm25_f = to_float(pm25)

        city = data.get("city")
        station = data.get("station")
        ts = data.get("timestamp")

        location = station or city or "Unknown-Location"
        printable = f"[{ts or 'NoTime'}] {location}: PM2.5={pm25_f if pm25_f is not None else 'NA'}"
        print(f"← recv (key={key}): {printable}")

        if pm25_f is not None and pm25_f > ALERT_THRESHOLD:
            print(f"!!! ALERT: Very Unhealthy PM2.5 detected ({pm25_f}) at {location} !!!")

if __name__ == "__main__":
    main()
