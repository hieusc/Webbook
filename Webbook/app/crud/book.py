def get_all_books(cur):
    cur.execute("SELECT * FROM public.sach ORDER BY id;")
    return cur.fetchall()


def get_book_by_id(cur, id: int):
    cur.execute("SELECT * FROM public.sach WHERE id = %s;", (id,))
    return cur.fetchone()


def get_book_by_name(cur, name: str):
    cur.execute("SELECT * FROM public.sach WHERE name = %s;", (name,))
    return cur.fetchone()


def create_book(cur, book_data):
    cur.execute(
        "INSERT INTO public.sach (name, author, type, price, soluong) "
        "VALUES (%s, %s, %s, %s, %s) RETURNING *;",
        (book_data.name, book_data.author, book_data.type, book_data.price, book_data.soluong),
    )
    return cur.fetchone()


def update_book(cur, id: int, book_data):
    cur.execute(
        "UPDATE public.sach SET name = %s, author = %s, type = %s, price = %s, soluong = %s "
        "WHERE id = %s RETURNING *;",
        (book_data.name, book_data.author, book_data.type, book_data.price, book_data.soluong, id),
    )
    return cur.fetchone()


def delete_book(cur, id: int):
    cur.execute("DELETE FROM public.sach WHERE id = %s;", (id,))
