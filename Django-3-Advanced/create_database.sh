set -eu

set -a
. ./.env
set +a

NAME=$(printf '%s' "$NAME" | tr -d '\r')
USER=$(printf '%s' "$USER" | tr -d '\r')
PASSWORD=$(printf '%s' "$PASSWORD" | tr -d '\r')
HOST=$(printf '%s' "$HOST" | tr -d '\r')
PORT=$(printf '%s' "$PORT" | tr -d '\r')

PSQL=""

if command -v psql >/dev/null 2>&1 && psql --version >/dev/null 2>&1; then
	PSQL=$(command -v psql)
fi

if [ -z "$PSQL" ] && command -v psql.exe >/dev/null 2>&1; then
	PSQL=$(command -v psql.exe)
fi

if [ -z "$PSQL" ] && command -v cmd.exe >/dev/null 2>&1; then
	PSQL=$(cmd.exe /c where psql.exe 2>/dev/null | tr -d '\r' | head -n 1)
fi

if [ -z "$PSQL" ] && [ -d "/mnt/c/Program Files/PostgreSQL" ]; then
	PSQL=$(find "/mnt/c/Program Files/PostgreSQL" -name psql.exe -type f 2>/dev/null | head -n 1)
fi

if [ -z "$PSQL" ] && [ -d "/mnt/c/Program Files (x86)/PostgreSQL" ]; then
	PSQL=$(find "/mnt/c/Program Files (x86)/PostgreSQL" -name psql.exe -type f 2>/dev/null | head -n 1)
fi

if [ -z "$PSQL" ]; then
	echo "Error: no usable PostgreSQL client was found. Install postgresql-client in WSL or PostgreSQL on Windows." >&2
	exit 1
fi

"$PSQL" -h "${HOST:-localhost}" -p "${PORT:-5432}" -U postgres -d postgres -v dbname="$NAME" -v dbuser="$USER" -v dbpass="$PASSWORD" <<'EOF'
-- Kick out other sessions
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE datname = :'dbname' AND pid <> pg_backend_pid();

-- Reset everything safely
DROP DATABASE IF EXISTS :"dbname";
DROP USER IF EXISTS :"dbuser";

-- Recreate database and user
CREATE DATABASE :"dbname";
CREATE USER :"dbuser" WITH ENCRYPTED PASSWORD :'dbpass';
GRANT ALL PRIVILEGES ON DATABASE :"dbname" TO :"dbuser";

-- Connect directly to the new database to fix schema permissions
\connect :"dbname"

-- CRITICAL FIX FOR POSTGRESQL 15+:
GRANT ALL ON SCHEMA public TO :"dbuser";
ALTER SCHEMA public OWNER TO :"dbuser";
EOF
