import socket
import sys


def whois_query(domain):
    try:
        # Conecta ao servidor WHOIS padrão
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("whois.verisign-grs.com", 43))
        s.send((domain + "\r\n").encode())

        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data

        s.close()
        return response.decode(errors="ignore")
    except Exception as e:
        return f"[!] Erro ao realizar consulta WHOIS: {str(e)}"


if __name__ == "__main__":
    print("""
██╗    ██╗██╗  ██╗ ██████╗ ██╗███████╗    ███╗   ██╗ █████╗ ███╗   ███╗██╗███╗   ██╗ ██████╗ 
██║    ██║██║  ██║██╔═══██╗██║██╔════╝    ████╗  ██║██╔══██╗████╗ ████║██║████╗  ██║██╔════╝ 
██║ █╗ ██║███████║██║   ██║██║█████╗      ██╔██╗ ██║███████║██╔████╔██║██║██╔██╗ ██║██║  ███╗
██║███╗██║██╔══██║██║   ██║██║██╔══╝      ██║╚██╗██║██╔══██║██║╚██╔╝██║██║██║╚██╗██║██║   ██║
╚███╔███╔╝██║  ██║╚██████╔╝██║███████╗    ██║ ╚████║██║  ██║██║ ╚═╝ ██║██║██║ ╚████║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚══════╝    ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

WHOIS Tool | Ethical Hacking Edition | By Bellani
    """
    )

    if len(sys.argv) != 2:
        print("[!] Uso: python whois.py dominio.com")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"\n[+] Consultando WHOIS de: {domain}\n")
    result = whois_query(domain)
    print(result)
