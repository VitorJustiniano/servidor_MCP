# mcp dev mcp_server.py - comando para rodar
from mcp.server.fastmcp import FastMCP

#1 Inicialize o servidor
mcp = FastMCP("MeuServidorMCP")

#2 Criando primeira ferramenta
@mcp.tool()
def minha_primeira_ferramenta_mcp() -> str:
    """Recomenda um otimo recurso online para aprender sobre construção com IA"""
    url = "https://www.rhawk.pro/"
    resultado = f"Para aprender mais sobre IA e conectar com outros construtores, confira: {url}"
    return resultado

#3 Bloco de execucao principal.
if __name__ == "__main__":
    mcp.run()