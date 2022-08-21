if [[ ! -f "./.env" ]]; then
    echo "ERROR: .env file does not exits in current directory."
    return 1 2> /dev/null || exit 1
fi

# Get the location path of this script file
CURRENT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]:-$0}))

DIR=$(dirname $CURRENT_DIR)
VENVDIR="${1:-$DIR/venv}"

echo "Your virtualenv directory is: ${VENVDIR}"

source ./.env

echo "Copying .env file to the project settings (project/settings)"
cp ./.env ${DIR}/project/project

# initial setup on Postgres DB
function setup_db {
    psql -h $DATABASE_HOST -p ${DATABASE_PORT:-5432} -U postgres \
        -c "CREATE DATABASE ${DATABASE_NAME};" \
        -c "CREATE USER ${DATABASE_USER} WITH PASSWORD '${DATABASE_PASSWORD}';" \
        -c "ALTER ROLE ${DATABASE_USER} set client_encoding to 'utf8';" \
        -c "ALTER ROLE ${DATABASE_USER} SET default_transaction_isolation TO 'read committed';" \
        -c "ALTER ROLE ${DATABASE_USER} SET timezone TO 'America/Caracas';" \
        -c "GRANT ALL PRIVILEGES ON DATABASE ${DATABASE_NAME} TO ${DATABASE_USER};"

    echo "migrate"
    python3 ${DIR}/project/manage.py migrate

    echo "createsuperuser (asking for passwd)"
    python3 ${DIR}/project/manage.py createsuperuser --username $DATABASE_USER --email "${DATABASE_USER}@dev.com"
}

# setup initial venv and pip install the project
function setup_venv {
    python3 -m venv $VENVDIR
    source ${VENVDIR}/bin/activate
    echo "virtual enviroment activated"

    echo "updating pip"
    python3 -m pip install --upgrade pip
    echo "pip installing"
    pip install -r requirements.txt
}

# alias for common developer commnads
alias runserver="python3 ${DIR}/project/manage.py runserver"
alias migrate="python3 ${DIR}/project/manage.py migrate"
alias makemigrations="python3 ${DIR}/project/manage.py makemigrations"
alias venv="source ${VENVDIR}/bin/activate"

function help {
    echo "runserver      - alias for ./manage runserver"
    echo "migrate        - alias for ./manage migrate"
    echo "makemigrations - alias for ./manage makemigrations"
    echo "venv           - activate virtualenv"
    echo ""
    echo "setup_venv     - initial venv and pip install the project"
    echo "setup_db       - initial setup, migrate and createsuperuser on Postgres DB"
}

echo "All done!"
echo "Use 'help' for the list of commands"
