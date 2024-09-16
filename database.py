from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://admin:Aje-1496@siwesprov2.c3awiqe8220p.eu-north-1.rds.amazonaws.com/siwespro?charset=utf8mb4"

engine = create_engine(db_connection_string)

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      jobs = []
      for row in result.mappings().all():
          jobs.append(dict(row))
      return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), {"val": id})
        rows = result.mappings().all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0])
        
def add_application_to_db(job_id, data):
  data = dict(data)
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(
      query, {
        "job_id": job_id,
        "full_name": data["full_name"],
        "email": data["email"],
        "linkedin_url": data["linkedin_url"],
        "education": data["education"],
        "work_experience": data["work_experience"],
        "resume_url": data["resume_url"]
      })
    conn.commit()