from unittest.mock import patch

class TodoService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_todo_details(self, todo_id):
        todo = self.api_client.get_todo(todo_id)
        # Lógica de negocio adicional
        todo['title'] = todo['title'].title()
        return todo

    def add_todo(self, title, completed=False):
        data = {
            'title': title,
            'completed': completed
        }
        return self.api_client.create_todo(data)

    def complete_todo(self, todo_id):
        todo = self.api_client.get_todo(todo_id)
        if not todo['completed']:
            todo['completed'] = True
            return self.api_client.update_todo(todo_id, todo)
        return todo

    def remove_todo(self, todo_id):
        return self.api_client.delete_todo(todo_id)


# Función de prueba fuera de la clase
def test_complete_todo_patching(mocker):
    # Crear un cliente API simulado
    mock_api_client = mocker.Mock()

    # Instanciar el servicio de Todo con el cliente simulado
    todo_service = TodoService(mock_api_client)

    # Configurar el comportamiento del cliente simulado
    mock_api_client.get_todo.return_value = {
        "id": 1,
        "title": "Incomplete Todo",
        "completed": False
    }
    mock_api_client.update_todo.return_value = {
        "id": 1,
        "title": "Incomplete Todo",
        "completed": True
    }

    # Llamar al método a probar
    todo = todo_service.complete_todo(1)

    # Asserts
    assert todo["completed"] == True
    mock_api_client.get_todo.assert_called_once_with(1)
    mock_api_client.update_todo.assert_called_once_with(1, {
        "id": 1,
        "title": "Incomplete Todo",
        "completed": True
    })
