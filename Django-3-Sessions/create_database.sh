# set -a
# source .env
# set +a

psql -U postgres <<EOF
-- Kick out other sessions
SELECT pg_terminate_backend(pid) 
FROM pg_stat_activity 
WHERE datname = '$NAME' AND pid <> pg_backend_pid();

-- Reset everything safely
DROP DATABASE IF EXISTS $NAME;
DROP USER IF EXISTS $USER;

-- Recreate database and user
CREATE DATABASE $NAME;
CREATE USER $USER WITH ENCRYPTED PASSWORD '$PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE $NAME TO $USER;

-- Connect directly to the new database to fix schema permissions
\c $NAME

-- CRITICAL FIX FOR POSTGRESQL 15+:
GRANT ALL ON SCHEMA public TO $USER;
ALTER SCHEMA public OWNER TO $USER;
EOF
