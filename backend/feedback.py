# backend/feedback.py
from db_connection import get_db_connection

def save_feedback(feedback_data):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = '''
        INSERT INTO feedback (user_id, recommendation_id, feedback_type)
        VALUES (%s, %s, %s)
    '''
    cursor.execute(query, (feedback_data['user_id'], feedback_data['recommendation_id'], feedback_data['feedback_type']))
    connection.commit()
    connection.close()
