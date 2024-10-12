from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from .db.database import engine, get_db
from .questions import question_model
from .questions.questions_schemas import QuestionRequest, QuestionResponse
from .questions.question_model import Question
from sqlalchemy.orm import Session
from datetime import datetime
from .trivia import Question, Quiz

app = FastAPI()
quiz = Quiz()

question_model.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return { 'message': 'Server alive', 'time': datetime.now() }

@app.get('/questions', status_code=status.HTTP_200_OK, response_model=List[QuestionResponse])
def get_all_questions(db: Session = Depends(get_db)):
    all_questions = db.query(Question).all()
    return all_questions

@app.post("/questions", response_model=QuestionResponse)
def create_question(question: QuestionRequest, db: Session = Depends(get_db)):
    new_question = Question(
        description=question.description,
        options=question.options,
        correct_answer=question.correct_answer  # Añadir la respuesta correcta
    ) 
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

@app.patch("/questions/{id}", response_model=QuestionResponse)
def update_question(id: int, question_update: QuestionRequest, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == id).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    
    # Actualiza solo los campos que se envían en el cuerpo de la solicitud
    if question_update.description:
        question.description = question_update.description
    if question_update.options:
        question.options = question_update.options
    if question_update.correct_answer:
        question.correct_answer = question_update.correct_answer

    db.commit()
    db.refresh(question)
    return question


@app.delete("/questions/{id}", response_model=QuestionResponse)
def delete_question(id: int, db: Session = Depends(get_db)):
    # Busca la pregunta por ID
    question = db.query(Question).filter(Question.id == id).first()
    
    if not question:
        # Si no se encuentra la pregunta, lanza una excepción 404
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    
    db.delete(question)  # Elimina la pregunta de la base de datos
    db.commit()  # Confirma los cambios en la base de datos
    return question  # Devuelve la pregunta eliminada

