from core.database import get_connection
from datetime import datetime

def save_alert(account, score, scenarios):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO alerts (account, score, scenarios, created_at) VALUES (?,?,?,?)",
        (
            account,
            score,
            ",".join(scenarios),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


def load_alerts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT account, score, scenarios, created_at FROM alerts ORDER BY id DESC LIMIT 50"
    )
    rows = cur.fetchall()
    conn.close()

    return rows