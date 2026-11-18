# Lưu ý: "user" là từ khoá của PostgreSQL nên luôn ghi kèm schema: public.user


def get_all_user(cur):
    cur.execute("SELECT * FROM public.user ORDER BY id;")
    return cur.fetchall()


def get_id_user(cur, id: int):
    cur.execute("SELECT * FROM public.user WHERE id = %s;", (id,))
    return cur.fetchone()


def get_name_user(cur, name: str):
    cur.execute("SELECT * FROM public.user WHERE name = %s;", (name,))
    return cur.fetchone()


def get_phone_user(cur, phone: str):
    cur.execute("SELECT * FROM public.user WHERE phone = %s;", (phone,))
    return cur.fetchone()


def get_email_user(cur, email: str):
    cur.execute("SELECT * FROM public.user WHERE email = %s;", (email,))
    return cur.fetchone()


def get_tk_user(cur, tk: str):
    cur.execute("SELECT * FROM public.user WHERE tk = %s;", (tk,))
    return cur.fetchone()


def create_user(cur, user):
    cur.execute(
        "INSERT INTO public.user (name, age, phone, email) VALUES (%s, %s, %s, %s) RETURNING *;",
        (user.name, user.age, user.phone, user.email),
    )
    return cur.fetchone()


def update_user(cur, id: int, user):
    cur.execute(
        "UPDATE public.user SET name = %s, age = %s, phone = %s, email = %s "
        "WHERE id = %s RETURNING *;",
        (user.name, user.age, user.phone, user.email, id),
    )
    return cur.fetchone()


def delete_user(cur, id: int):
    cur.execute("DELETE FROM public.user WHERE id = %s;", (id,))


def create_tk(cur, tk: str, mk_hashed: str):
    # mk_hashed: mật khẩu ĐÃ MÃ HOÁ, không truyền mật khẩu gốc vào đây
    cur.execute(
        "INSERT INTO public.user (tk, mk) VALUES (%s, %s) RETURNING *;",
        (tk, mk_hashed),
    )
    return cur.fetchone()
