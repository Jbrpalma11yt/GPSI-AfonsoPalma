psi_19_11/                                                 # Pasta principal do programa
└──├── Pack_car/                                   # Pacote principal que contém alógica da aplicação │ 
   │   ├── app/                               # Diretório que contém o arquivo principal da aplicação │ 
   │   │    └── main.py                      # Ponto de entrada da aplicação
   │   ├── create/                        # Diretório para scripts de criação de registros │  
   │   │    ├── car_create.py            # Script para criar um novo carro │ 
   │   │    └── car_insert.py          # Script para inserir dados de carro no banco
   │   ├── delet/                     # Diretório para scripts de exclusão de registros │  
   │   │    ├─ ─Car_delete.py         # Script para excluir um carro específico │
   │   │    ├── CarroAno_delete.py     # Script para excluir carros por ano │
   │   │    └── Matriculas_delete.py    # Script para excluir registros de matrículas │ 
   │   ├── drops_Test/                              # Diretório para testes de exclusão │
   │   │     └── drops.py                              # Script para testar a exclusão de registros │ 
   │   ├── read/                                        # Diretório para scripts de leitura de registros │ 
   │   │    ├── car_Read.py                              # Script para ler dados de carros │ 
   │   │    ├── matriculas_Read. py                       # Script para ler dados de matrículas │  
   │   │    └── Select.py                                  # Script para selecionar registros específicos │ 
   │   └── update/                                         # Diretório para scripts de atualização de registros │ 
   │        └── Car_update.py                              # Script para atualizar dados de um carro │
   ├── Pack_car.db                                         # Banco de dados principais da aplicação │ 
   ├── README.md                                            # Este arquivo, que contém informações sobre o projeto │
   └── Seu_banco_de_dados.db                                # Outro banco de dados utilizado no projeto