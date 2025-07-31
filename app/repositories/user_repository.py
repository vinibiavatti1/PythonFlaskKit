from app import database
from app.entities.user_entity import UserEntity
from app.filters.user_filter import UserFilter
from typing import Any


def insert_user(entity: UserEntity) -> UserEntity:
    with database.connect() as db:
        sql = f"""
            INSERT INTO users (name, email, password_hash, role, email_verified, hash)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor = db.cursor()
        cursor.execute(sql, (entity.name, entity.email, entity.password_hash, entity.role, entity.email_verified, entity.hash))
        db.commit()
        entity.id = cursor.lastrowid
        return entity


def update_user(entity: UserEntity) -> UserEntity:
    with database.connect() as db:
        sql = f"""
            UPDATE users
            SET name = %s, active = %s, role = %s, email_verified = %s, last_login = %s, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
        """
        cursor = db.cursor()
        cursor.execute(sql, (entity.name, entity.active, entity.role, entity.email_verified, entity.last_login, entity.id))
        db.commit()
        return entity


def get_user(id: int) -> UserEntity | None:
    with database.connect() as db:
        sql = f"""
            SELECT * FROM users WHERE id = %s
        """
        cursor = db.cursor(dictionary=True)
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        if result is None:
            return None
        entity = UserEntity()
        entity.__dict__.update(result)
        return entity


def list_users(filters: UserFilter) -> list[UserEntity]:
    with database.connect() as db:
        sql = f"""
            SELECT * FROM users WHERE 1 = 1
        """
        data: list[Any] = []
        if filters.name is not None:
            sql += f' AND name = %s'
            data.append(filters.name)
        if filters.email is not None:
            sql += f' AND email = %s'
            data.append(filters.email)
        if filters.role is not None:
            sql += f' AND role = %s'
            data.append(filters.role)
        if filters.password_hash is not None:
            sql += f' AND password_hash = %s'
            data.append(filters.password_hash)
        if filters.email_verified is not None:
            sql += f' AND email_verified = %s'
            data.append(filters.email_verified)
        if filters.active is not None:
            sql += f' AND active = %s'
            data.append(filters.active)
        if filters.hash is not None:
            sql += f' AND hash = %s'
            data.append(filters.hash)
        sql += ' ORDER BY name'
        cursor = db.cursor(dictionary=True)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        entities = []
        for row in result:
            entity = UserEntity()
            entity.__dict__.update(row)
            entities.append(entity)
        return entities
