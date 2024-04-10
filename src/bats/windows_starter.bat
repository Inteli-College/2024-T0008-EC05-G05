@echo off

rem Obter o caminho do diretório atual
set "current_dir_path=%cd%"
set "current_project_path=%current_dir_path%"

echo %current_project_path%

echo Sistema operacional: Windows

rem Inserir código específico para Windows aqui

cd "%current_project_path%"

rem Criar e ativar o ambiente virtual
python -m venv venv
call venv\Scripts\activate

rem Navegar até o diretório contendo requirements.txt e instalar as dependências
cd "%current_project_path%"
pip install -r requirements.txt

pip uninstall serial -y

rem Iniciar o Front-end
start cmd /k "echo Front-end && cd src/frontend && npm i && npm start"

rem Inicar a API do robo
start cmd /k "echo API Robo && cd src/backend/api && python bot.py"

rem Inicar a API do estoque
start cmd /k "echo  && cd src/backend/api && python stock.py"