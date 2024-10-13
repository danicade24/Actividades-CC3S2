from db.database import SessionLocal, Base, engine
from src.questions.question_model import Question as DBQuestion

def add_initial_questions(db):
    # Lista de preguntas a agregar
    questions = [
        # Preguntas de nivel fácil
        DBQuestion(description="¿Cuánto es 3 + 5?", 
                   options=["9", "10", "8", "7"], 
                   correct_answer="8", level="easy"),
        DBQuestion(description="¿Cuál es el planeta más cercano al Sol?", 
                   options=["Tierra", "Marte", "Venus", "Mercurio"], 
                   correct_answer="Mercurio", level="easy"),
        DBQuestion(description="¿Cuánto es 10 - 4?", 
                   options=["5", "6", "4", "7"], 
                   correct_answer="6", level="easy"),
        DBQuestion(description="¿Qué animal es conocido como el rey de la selva?", 
                   options=["León", "Tigre", "Elefante", "Canguro"], 
                   correct_answer="León", level="easy"),

        # Preguntas de nivel medio
        DBQuestion(description="¿Cuál es el elemento químico con el símbolo Fe?", 
                   options=["Fósforo", "Hierro", "Flúor", "Francio"], 
                   correct_answer="Hierro", level="medium"),
        DBQuestion(description="¿Cuánto es 17 + 28?", 
                   options=["44", "45", "46", "47"], 
                   correct_answer="45", level="medium"),
        DBQuestion(description="¿Cuál es el país más grande del mundo?", 
                   options=["Estados Unidos", "Canadá", "Rusia", "China"], 
                   correct_answer="Rusia", level="medium"),
        DBQuestion(description="¿Cuál es el océano más grande del mundo?", 
                   options=["Atlántico", "Pacífico", "Índico", "Ártico"], 
                   correct_answer="Pacífico", level="medium"),
        DBQuestion(description="¿Cuánto es 100 - 47?", 
                   options=["51", "53", "57", "63"], 
                   correct_answer="53", level="medium"),

        # Preguntas de nivel difícil
        DBQuestion(description="¿Cuánto es 234 + 567?", 
                   options=["789", "801", "800", "812"], 
                   correct_answer="801", level="hard"),
        DBQuestion(description="¿En qué año comenzó la Primera Guerra Mundial?", 
                   options=["1912", "1914", "1916", "1918"], 
                   correct_answer="1914", level="hard"),
        DBQuestion(description="¿Cuál es el órgano más grande del cuerpo humano?", 
                   options=["Hígado", "Piel", "Cerebro", "Corazón"], 
                   correct_answer="Piel", level="hard"),
        DBQuestion(description="¿Qué protocolo se utiliza para enviar correos electrónicos?", 
                   options=["FTP", "SMTP", "HTTP", "IMAP"], 
                   correct_answer="SMTP", level="hard"),
        DBQuestion(description="¿Cuánto es 25 x 19?", 
                   options=["475", "480", "485", "490"], 
                   correct_answer="475", level="hard")
    ]
    
    # Agrega las preguntas a la base de datos
    db.add_all(questions)
    db.commit()
    print("Preguntas iniciales agregadas a la base de datos.")

def init_db():
    Base.metadata.create_all(bind=engine)  # Crea las tablas en la base de datos
    db = SessionLocal()
    try:
        add_initial_questions(db)  # Agrega preguntas
    finally:
        db.close()

if __name__ == "__main__":
    init_db()