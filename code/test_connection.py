import psycopg2
import os
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

print("=== TESTE DE CONEXÃO POSTGRESQL ===")

try:
    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='postgres',
        user='postgres',
        password='postgres'  # Tente esta senha primeiro
    )
    print('✅ CONEXÃO BEM-SUCEDIDA!')
    
    # Teste adicional
    cur = conn.cursor()
    cur.execute('SELECT version();')
    version = cur.fetchone()[0]
    print(f'📋 PostgreSQL Version: {version}')
    
    cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    databases = cur.fetchall()
    print("🗃️ Bancos disponíveis:")
    for db in databases:
        print(f"   - {db[0]}")
    
    cur.close()
    conn.close()
    
except Exception as e:
    print(f'❌ ERRO: {e}')
    print("\n🔍 Tentando descobrir a senha...")
    
    # Método para descobrir a senha
    import subprocess
    result = subprocess.run([
        'docker', 'inspect', 'postgres_postgres.1.nscbiiq9hvroc2tn5c3998d1j',
        '--format', '{{range .Config.Env}}{{.}}{{\"\\n\"}}{{end}}'
    ], capture_output=True, text=True)
    
    passwords_found = []
    for line in result.stdout.split('\n'):
        if 'PASSWORD' in line.upper():
            passwords_found.append(line)
    
    if passwords_found:
        print("🔐 Variáveis de senha encontradas no container:")
        for pwd in passwords_found:
            print(f"   {pwd}")
    else:
        print("⚠️ Nenhuma senha encontrada nas variáveis do container")
        print("💡 Tente estas senhas comuns:")
        for common_pwd in ['postgres', 'password', 'supabase', 'admin', 'root']:
            print(f"   - {common_pwd}")