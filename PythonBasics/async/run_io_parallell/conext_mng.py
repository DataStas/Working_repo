import asyncio


class TransactionCtx:
    def __init__(self, conn):
        self.conn = conn
    
    async def __aenter__(self):
        await self.conn.execute('BEGIN')
        print('entering context')
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        command = 'ROLLBACK' if exc else 'COMMIT'
        await self.conn.execute(command)
        print('exiting context')

async def main():
    conn = await connect(...)
    async with TransactionCtx(conn) as transaction:


if __name__ == '__main__':
    asyncio.run(main())