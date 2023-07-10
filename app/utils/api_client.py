import requests



def verify_user_existence(user_id: int) -> bool:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    return response.status_code == 200


def get_user_data_from_external_api(user_id: int) -> dict:
    # Obtener los datos del usuario desde la API externa
    # y retornar un diccionario con los datos necesarios
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)

    user_data = {
        "user_id": response.json()["id"],
        "name": response.json()["name"],
        "username": response.json()["username"],
        "email": response.json()["email"],
        # Obtener los demás datos necesarios desde la API externa
    }
    return user_data