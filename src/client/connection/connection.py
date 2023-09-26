import asyncio


class ConnectToServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def send_and_receive_file(self, message):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        print(f"Send: {message}")
        writer.write(message.encode())
        await writer.drain()

        data = await reader.read(100)

        print("Close the connection")
        writer.close()
        await writer.wait_closed()


async def send_and_receive_file(encrypted):
    if encrypted:
        with open("text_file.txt", "rb") as file:
            original_data = file.read()

    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    writer.write(original_data)
    await writer.drain()

    modified_data = await reader.read(100)

    with open("server_text_file.txt", "wb") as file:
        file.write(modified_data)

    print("File received and saved as 'server_text_file.txt'")

    writer.close()
    await writer.wait_closed()
