# Hello!

web: gunicorn hello2:app --log-file -
worker: python main.py


cython==0.29.12
pywin32==303
pywin32==302
pypiwin32-223
pypiwin32==223
pywinpty==1.1.6

pysam
pgen
cargo
rust
cython --> https://pypi.org/project/Cython/#files
pywinpty
pywin32 --> https://pypi.org/project/pywin32/302/#files


client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

client.run(token)