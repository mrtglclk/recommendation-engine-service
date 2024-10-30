# backend/recommendation.py
from db_connection import get_db_connection

def get_recommendations(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = '''
        SELECT menu_item FROM menus 
        WHERE user_id = %s OR user_preferences LIKE %s
    '''
    cursor.execute(query, (user_id, f"%{user_id}%"))
    recommendations = cursor.fetchall()
    connection.close()

    return [item['menu_item'] for item in recommendations]
