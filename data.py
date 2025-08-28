class TestData:
    CORECT_LOGIN = "Frimpong"
    CORECT_PASSWORD = "4321"
    CORECT_NAME = "Jordan"

    ORDER_DATA = {
        "first_name": "Naruto",
        "last_name": "Uchiha",
        "address1": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha"
    }

    MESSAGE_CONFLICT = {"message": "Этот логин уже используется"}
    MESSAGE_BAD_REQUEST = {"message": "Недостаточно данных для создания учетной записи"}
    MESSAGE_NOT_FOUND = {"message": "Учетная запись не найдена"}