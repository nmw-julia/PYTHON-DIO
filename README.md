1. Introdução
Este projeto faz parte da formação em Cibersegurança da DIO e tem como objetivo explorar o funcionamento interno de duas das ameaças mais comuns no cenário digital: Ransomware e Keylogger. O foco é entender a lógica de programação por trás dessas ameaças para fortalecer estratégias de defesa e resposta a incidentes.
AVISO DE SEGURANÇA: Este projeto foi desenvolvido em ambiente controlado para fins estritamente educacionais. O uso desses scripts em sistemas sem autorização é ilegal e antiético.

3. Descrição Técnica
2.1. Ransomware Simulado
O script de Ransomware utiliza a biblioteca cryptography (algoritmo Fernet/AES) para realizar a criptografia simétrica de arquivos em um diretório específico.
Mecanismo: O código gera uma chave única, varre o diretório alvo e sobrescreve o conteúdo dos arquivos com sua versão cifrada.
Vetor de Ataque: Simula o sequestro de dados onde apenas a posse da chave original permite a recuperação.

2.2. Keylogger Simulado
O Keylogger utiliza a biblioteca pynput para monitorar eventos do teclado em nível de sistema.
Mecanismo: O script registra cada tecla pressionada (incluindo teclas especiais como Space, Enter e Shift) e armazena os dados cronologicamente em um arquivo oculto key_log.txt.
Furtividade: O script pode ser configurado para rodar em segundo plano, demonstrando como credenciais podem ser capturadas de forma silenciosa.

5. Implementação e Testes
Pré-requisitos

bash
pip install cryptography pynput

Comandos de Execução
Para o Ransomware: Certifique-se de ter uma pasta de teste com arquivos .txt.

bash
python ransomw.py

Para o Keylogger: Inicie o monitoramento e digite em qualquer janela.

bash
python keylogger.py

5. Análise Defensiva e Mitigação
A parte mais importante deste desafio é entender como nos proteger. Com base nos experimentos, as seguintes medidas são recomendadas:
Contra Ransomware:
Backups Offline: Manter cópias de segurança fora da rede (estratégia 3-2-1).
Monitoramento Heurístico: Utilizar antivírus/EDR que detectem padrões de criptografia em massa em curto espaço de tempo.
Controle de Permissões: Limitar o acesso de escrita de usuários a pastas críticas.
Contra Keyloggers:
Teclados Virtuais: Utilizar teclados em tela para inserção de senhas bancárias.
Autenticação de Dois Fatores (2FA): Mesmo que a senha seja capturada, o segundo fator protege a conta.
Análise de Processos: Monitorar processos desconhecidos que consomem recursos de entrada de dados.
6. Conclusão
A prática demonstrou que malwares potentes podem ser construídos com poucas linhas de código, o que reforça a necessidade de camadas de segurança robustas e, acima de tudo, a conscientização dos usuários sobre os vetores de entrada (Phishing e Engenharia Social).
