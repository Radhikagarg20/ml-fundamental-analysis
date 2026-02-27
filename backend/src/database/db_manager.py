from sqlalchemy import create_engine, text
from config.settings import DB_CONFIG

def get_engine():
    db_url = f"mysql+pymysql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
    return create_engine(db_url)

def save_analysis(company_id, score, pros, cons):
    engine = get_engine()

    query = text("""
        INSERT INTO ml (company_id, score, pros, cons)
        VALUES (:company_id, :score, :pros, :cons)
    """)

    with engine.connect() as conn:
        conn.execute(query, {
            "company_id": company_id,
            "score": score,
            "pros": ", ".join(pros),
            "cons": ", ".join(cons)
        })
        conn.commit()