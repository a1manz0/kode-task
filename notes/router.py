from fastapi import APIRouter, Depends
from database import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert
from notes.models import note
from notes.schemas import NoteCreate
from auth.models import User
from auth.auth import current_user

from pyaspeller import YandexSpeller


speller = YandexSpeller()

router = APIRouter(prefix="/notes", tags=["Notes2"])


@router.get("/get_all")
async def get_notes(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    query = select(note).where(note.c.user == user.id)
    result = await session.execute(query)
    return {"notes": [list(result)[2:] for result in result.all()]}


@router.post("/add")
async def add_note(
    new_note: NoteCreate,
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session),
):
    content = new_note.content
    fixed_content = speller.spelled(content)
    stmt = insert(note).values(user=user.id, content=fixed_content)
    await session.execute(stmt)
    await session.commit()
    return {"status", "success"}
