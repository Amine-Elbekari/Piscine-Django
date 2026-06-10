set -eu

set -a
. ./.env
set +a

ENGINE=$(printf '%s' "$ENGINE" | tr -d '\r')
NAME=$(printf '%s' "$NAME" | tr -d '\r')
USER=$(printf '%s' "$USER" | tr -d '\r')
PASSWORD=$(printf '%s' "$PASSWORD" | tr -d '\r')
HOST=$(printf '%s' "$HOST" | tr -d '\r')
PORT=$(printf '%s' "$PORT" | tr -d '\r')

PASSWORD=$(printf '%s' "$PASSWORD" | sed "s/'/''/g")

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

"$PSQL" -h "${HOST:-localhost}" -p "${PORT:-5432}" -U postgres -d postgres -v dbname="$NAME" -v dbuser="$USER" <<PSQL_EOF
-- Kick out sessions for the requested database
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = :'dbname'
	AND pid <> pg_backend_pid();

-- Drop any previous copy of the requested database
DROP DATABASE IF EXISTS :"dbname";

-- Recreate the requested database and keep the user
DO \$\$
BEGIN
	IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${USER}') THEN
		EXECUTE 'ALTER USER ' || quote_ident('${USER}') || ' WITH ENCRYPTED PASSWORD ' || quote_literal('${PASSWORD}');
	ELSE
		EXECUTE 'CREATE USER ' || quote_ident('${USER}') || ' WITH ENCRYPTED PASSWORD ' || quote_literal('${PASSWORD}');
	END IF;
END
\$\$;

CREATE DATABASE :"dbname";
GRANT ALL PRIVILEGES ON DATABASE :"dbname" TO :"dbuser";

-- Connect directly to the new database to fix schema permissions
\connect :"dbname"

-- CRITICAL FIX FOR POSTGRESQL 15+:
GRANT ALL ON SCHEMA public TO :"dbuser";
ALTER SCHEMA public OWNER TO :"dbuser";
PSQL_EOF
