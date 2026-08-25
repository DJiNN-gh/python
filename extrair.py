import re
from pathlib import Path

# Caminhos corrigidos para "Documents" em vez de "Documentos"
DIRETORIO_RAIZ = "/Users/allan/Documents/Git/programas_c/1FAC"
ARQUIVO_SAIDA = "/Users/allan/Documents/Git/programas_c/1FAC/enunciados_extraidos.txt"

def extrair_enunciados(diretorio, saida):
    caminho_base = Path(diretorio)
    caminho_saida = Path(saida)
    
    # Linha de segurança: Garante que as pastas existam antes de criar o arquivo
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    
    # Cria ou sobrescreve o arquivo de saída
    with open(saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write("=== ENUNCIADOS EXTRAÍDOS ===\n\n")
        
        # Busca todos os arquivos .c recursivamente nas pastas e subpastas
        arquivos_c = list(caminho_base.rglob('*.c'))
        
        if not arquivos_c:
            print(f"Nenhum arquivo .c encontrado no diretório:\n{caminho_base}")
            return

        for arquivo_c in arquivos_c:
            try:
                with open(arquivo_c, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read()
                    
                    arquivo_saida.write(f"--- Lista/Pasta: {arquivo_c.parent.name} | Arquivo: {arquivo_c.name} ---\n")
                    
                    # Tenta capturar o primeiro bloco de comentário /* ... */
                    match_bloco = re.search(r'/\*(.*?)\*/', conteudo, re.DOTALL)
                    
                    if match_bloco:
                        enunciado = match_bloco.group(1).strip()
                        arquivo_saida.write(f"{enunciado}\n\n")
                    else:
                        # Se não achar /* */, tenta capturar linhas consecutivas com //
                        linhas_comentario = [linha.lstrip('/ ').strip('\n') for linha in conteudo.splitlines() if linha.strip().startswith('//')]
                        if linhas_comentario:
                            arquivo_saida.write('\n'.join(linhas_comentario) + "\n\n")
                        else:
                            arquivo_saida.write("[Nenhum comentário de enunciado encontrado]\n\n")
                            
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivo_c.name}: {e}")

    print(f"✅ Extração concluída! O arquivo foi salvo em:\n{saida}")

if __name__ == "__main__":
    extrair_enunciados(DIRETORIO_RAIZ, ARQUIVO_SAIDA)