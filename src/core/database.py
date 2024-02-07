from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from core.config import settings

engine = create_async_engine(url=settings.DATABASE_URL, echo=settings.db_echo)

async_session = async_sessionmaker(bind=engine)


async def get_session():
    async with async_session() as session:
        yield session